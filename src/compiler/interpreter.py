"""
Interpretador para o compilador Pascal.
Responsável por executar o código Pascal a partir da AST.
"""

import sys
from typing import Any, Dict, List, Optional, Union
from .ast_nodes import *

class RuntimeError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class ReturnException(Exception):
    def __init__(self, value: Any):
        self.value = value

class Environment:
    def __init__(self, parent: Optional['Environment'] = None):
        self.parent = parent
        self.variables: Dict[str, Any] = {}
        self.procedures: Dict[str, ProcedureDeclaration] = {}
        self.functions: Dict[str, FunctionDeclaration] = {}
    
    def define(self, name: str, value: Any):
        self.variables[name] = value
    
    def get(self, name: str) -> Any:
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise RuntimeError(f"Variável não definida: {name}")
    
    def set(self, name: str, value: Any):
        if name in self.variables:
            self.variables[name] = value
        elif self.parent and self.parent.has(name):
            self.parent.set(name, value)
        else:
            raise RuntimeError(f"Variável não definida: {name}")
    
    def has(self, name: str) -> bool:
        return name in self.variables or (self.parent and self.parent.has(name))
    
    def define_procedure(self, name: str, procedure: ProcedureDeclaration):
        self.procedures[name] = procedure
    
    def get_procedure(self, name: str) -> Optional[ProcedureDeclaration]:
        if name in self.procedures:
            return self.procedures[name]
        elif self.parent:
            return self.parent.get_procedure(name)
        else:
            return None
    
    def define_function(self, name: str, function: FunctionDeclaration):
        self.functions[name] = function
    
    def get_function(self, name: str) -> Optional[FunctionDeclaration]:
        if name in self.functions:
            return self.functions[name]
        elif self.parent:
            return self.parent.get_function(name)
        else:
            return None

class Interpreter:
    def __init__(self):
        self.global_env = Environment()
        self.current_env = self.global_env
        self.output_buffer = []
    
    def interpret(self, program: Program):
        try:
            # Primeiro, declarar todas as variáveis, procedimentos e funções
            for decl in program.declarations:
                self.execute_declaration(decl)
            
            # Executar o corpo principal
            self.execute_statement(program.body)
            
        except ReturnException:
            # Return no programa principal é ignorado
            pass
    
    def execute_declaration(self, declaration: ASTNode):
        if isinstance(declaration, VariableDeclaration):
            # Inicializar variável com valor padrão baseado no tipo
            if declaration.var_type == 'integer':
                default_value = 0
            elif declaration.var_type == 'real':
                default_value = 0.0
            elif declaration.var_type == 'boolean':
                default_value = False
            elif declaration.var_type == 'string':
                default_value = ""
            else:
                default_value = None
            
            if declaration.value:
                value = self.evaluate_expression(declaration.value)
            else:
                value = default_value
            
            self.current_env.define(declaration.name, value)
        
        elif isinstance(declaration, ArrayDeclaration):
            # Criar array com valores padrão
            if declaration.element_type == 'integer':
                default_value = 0
            elif declaration.element_type == 'real':
                default_value = 0.0
            elif declaration.element_type == 'boolean':
                default_value = False
            elif declaration.element_type == 'string':
                default_value = ""
            else:
                default_value = None
            
            array = [default_value] * declaration.size
            self.current_env.define(declaration.name, array)
        
        elif isinstance(declaration, ProcedureDeclaration):
            self.current_env.define_procedure(declaration.name, declaration)
        
        elif isinstance(declaration, FunctionDeclaration):
            self.current_env.define_function(declaration.name, declaration)
    
    def execute_statement(self, statement: Statement):
        if isinstance(statement, Block):
            for stmt in statement.statements:
                self.execute_statement(stmt)
        
        elif isinstance(statement, Assignment):
            value = self.evaluate_expression(statement.value)
            
            if isinstance(statement.target, Variable):
                self.current_env.set(statement.target.name, value)
            elif isinstance(statement.target, ArrayAccess):
                array_name = statement.target.array.name
                index = self.evaluate_expression(statement.target.index)
                array = self.current_env.get(array_name)
                
                if not isinstance(array, list):
                    raise RuntimeError(f"{array_name} não é um array")
                
                if not isinstance(index, int):
                    raise RuntimeError("Índice do array deve ser um inteiro")
                
                if index < 0 or index >= len(array):
                    raise RuntimeError(f"Índice do array fora dos limites: {index}")
                
                array[index] = value
        
        elif isinstance(statement, IfStatement):
            condition = self.evaluate_expression(statement.condition)
            if self.is_truthy(condition):
                self.execute_statement(statement.then_stmt)
            elif statement.else_stmt:
                self.execute_statement(statement.else_stmt)
        
        elif isinstance(statement, WhileStatement):
            while self.is_truthy(self.evaluate_expression(statement.condition)):
                self.execute_statement(statement.body)
        
        elif isinstance(statement, ForStatement):
            start_value = self.evaluate_expression(statement.start)
            end_value = self.evaluate_expression(statement.end)
            
            if not isinstance(start_value, int) or not isinstance(end_value, int):
                raise RuntimeError("Valores do loop FOR devem ser inteiros")
            
            # Criar nova variável de controle do loop
            previous_env = self.current_env
            self.current_env = Environment(previous_env)
            
            try:
                for i in range(start_value, end_value + 1):
                    self.current_env.define(statement.variable, i)
                    self.execute_statement(statement.body)
            finally:
                self.current_env = previous_env
        
        elif isinstance(statement, ProcedureCall):
            self.call_procedure(statement.name, statement.arguments)
        
        elif isinstance(statement, ReadlnStatement):
            for target in statement.targets:
                try:
                    if isinstance(target, Variable):
                        var_name = target.name
                        value = input(f"Digite o valor para {var_name}: ")
                        # Tentar converter para número se possível
                        try:
                            if '.' in value:
                                value = float(value)
                            else:
                                value = int(value)
                        except ValueError:
                            # Se não conseguir converter, manter como string
                            pass
                        
                        self.current_env.set(var_name, value)
                    
                    elif isinstance(target, ArrayAccess):
                        array_name = target.array.name
                        index = self.evaluate_expression(target.index)
                        
                        value = input(f"Digite o valor para {array_name}[{index}]: ")
                        # Tentar converter para número se possível
                        try:
                            if '.' in value:
                                value = float(value)
                            else:
                                value = int(value)
                        except ValueError:
                            # Se não conseguir converter, manter como string
                            pass
                        
                        array = self.current_env.get(array_name)
                        if not isinstance(array, list):
                            raise RuntimeError(f"{array_name} não é um array")
                        
                        if not isinstance(index, int):
                            raise RuntimeError("Índice do array deve ser um inteiro")
                        
                        if index < 0 or index >= len(array):
                            raise RuntimeError(f"Índice do array fora dos limites: {index}")
                        
                        array[index] = value
                    
                except EOFError:
                    break
        
        elif isinstance(statement, WritelnStatement):
            if statement.expressions:
                output_parts = []
                for expr in statement.expressions:
                    value = self.evaluate_expression(expr)
                    output_parts.append(str(value))
                
                output = ''.join(output_parts)
                print(output)
                self.output_buffer.append(output)
            else:
                print()
                self.output_buffer.append('')
        
        elif isinstance(statement, ReturnStatement):
            if statement.value:
                value = self.evaluate_expression(statement.value)
            else:
                value = None
            raise ReturnException(value)
    
    def evaluate_expression(self, expression: Expression) -> Any:
        if isinstance(expression, NumberLiteral):
            return expression.value
        
        elif isinstance(expression, StringLiteral):
            return expression.value
        
        elif isinstance(expression, BooleanLiteral):
            return expression.value
        
        elif isinstance(expression, Variable):
            return self.current_env.get(expression.name)
        
        elif isinstance(expression, ArrayAccess):
            array_name = expression.array.name
            index = self.evaluate_expression(expression.index)
            array = self.current_env.get(array_name)
            
            if not isinstance(array, list):
                raise RuntimeError(f"{array_name} não é um array")
            
            if not isinstance(index, int):
                raise RuntimeError("Índice do array deve ser um inteiro")
            
            if index < 0 or index >= len(array):
                raise RuntimeError(f"Índice do array fora dos limites: {index}")
            
            return array[index]
        
        elif isinstance(expression, BinaryOperation):
            left = self.evaluate_expression(expression.left)
            right = self.evaluate_expression(expression.right)
            
            if expression.operator == '+':
                return left + right
            elif expression.operator == '-':
                return left - right
            elif expression.operator == '*':
                return left * right
            elif expression.operator == '/':
                if right == 0:
                    raise RuntimeError("Divisão por zero")
                return left / right
            elif expression.operator == 'div':
                if right == 0:
                    raise RuntimeError("Divisão por zero")
                return int(left) // int(right)
            elif expression.operator == 'mod':
                if right == 0:
                    raise RuntimeError("Divisão por zero")
                return int(left) % int(right)
            elif expression.operator == '=':
                return left == right
            elif expression.operator == '<>':
                return left != right
            elif expression.operator == '<':
                return left < right
            elif expression.operator == '>':
                return left > right
            elif expression.operator == '<=':
                return left <= right
            elif expression.operator == '>=':
                return left >= right
            elif expression.operator == 'and':
                return self.is_truthy(left) and self.is_truthy(right)
            elif expression.operator == 'or':
                return self.is_truthy(left) or self.is_truthy(right)
            else:
                raise RuntimeError(f"Operador binário não suportado: {expression.operator}")
        
        elif isinstance(expression, UnaryOperation):
            operand = self.evaluate_expression(expression.operand)
            
            if expression.operator == '+':
                return +operand
            elif expression.operator == '-':
                return -operand
            elif expression.operator == 'not':
                return not self.is_truthy(operand)
            else:
                raise RuntimeError(f"Operador unário não suportado: {expression.operator}")
        
        elif isinstance(expression, FunctionCall):
            return self.call_function(expression.name, expression.arguments)
        
        else:
            raise RuntimeError(f"Tipo de expressão não suportado: {type(expression)}")
    
    def call_procedure(self, name: str, arguments: List[Expression]):
        procedure = self.current_env.get_procedure(name)
        
        if procedure is None:
            raise RuntimeError(f"Procedimento não definido: {name}")
        
        if len(arguments) != len(procedure.parameters):
            raise RuntimeError(f"Número incorreto de argumentos para {name}")
        
        # Criar novo ambiente para a execução do procedimento
        previous_env = self.current_env
        self.current_env = Environment(previous_env)
        
        try:
            # Avaliar argumentos e definir parâmetros
            for i, param in enumerate(procedure.parameters):
                arg_value = self.evaluate_expression(arguments[i])
                self.current_env.define(param.name, arg_value)
            
            # Executar corpo do procedimento
            self.execute_statement(procedure.body)
        
        except ReturnException:
            # Return em procedimento é ignorado
            pass
        
        finally:
            self.current_env = previous_env
    
    def call_function(self, name: str, arguments: List[Expression]) -> Any:
        function = self.current_env.get_function(name)
        
        if function is None:
            raise RuntimeError(f"Função não definida: {name}")
        
        if len(arguments) != len(function.parameters):
            raise RuntimeError(f"Número incorreto de argumentos para {name}")
        
        # Criar novo ambiente para a execução da função
        previous_env = self.current_env
        self.current_env = Environment(previous_env)
        
        try:
            # Avaliar argumentos e definir parâmetros
            for i, param in enumerate(function.parameters):
                arg_value = self.evaluate_expression(arguments[i])
                self.current_env.define(param.name, arg_value)
            
            # Executar corpo da função
            self.execute_statement(function.body)
            
            # Se chegou aqui sem return, retornar valor padrão
            if function.return_type == 'integer':
                return 0
            elif function.return_type == 'real':
                return 0.0
            elif function.return_type == 'boolean':
                return False
            elif function.return_type == 'string':
                return ""
            else:
                return None
        
        except ReturnException as e:
            return e.value
        
        finally:
            self.current_env = previous_env
    
    def is_truthy(self, value: Any) -> bool:
        if isinstance(value, bool):
            return value
        elif isinstance(value, (int, float)):
            return value != 0
        elif isinstance(value, str):
            return value != ""
        else:
            return value is not None
    
    def get_output(self) -> List[str]:
        return self.output_buffer.copy()
    
    def clear_output(self):
        self.output_buffer.clear()
