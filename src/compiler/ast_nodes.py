"""
Definições dos nós da Árvore Sintática Abstrata (AST)
"""

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union

class ASTNode(ABC):
    """Classe base para todos os nós da AST."""
    pass

class Expression(ASTNode):
    """Classe base para expressões."""
    pass

class Statement(ASTNode):
    """Classe base para comandos."""
    pass

# Expressões
class NumberLiteral(Expression):
    def __init__(self, value: Union[int, float]):
        self.value = value

class StringLiteral(Expression):
    def __init__(self, value: str):
        self.value = value
    
    def __str__(self):
        return f"StringLiteral({repr(self.value)})"

class BooleanLiteral(Expression):
    def __init__(self, value: bool):
        self.value = value

class Variable(Expression):
    def __init__(self, name: str):
        self.name = name

class ArrayAccess(Expression):
    def __init__(self, array: Expression, index: Expression):
        self.array = array
        self.index = index

class BinaryOperation(Expression):
    def __init__(self, left: Expression, operator: str, right: Expression):
        self.left = left
        self.operator = operator
        self.right = right

class UnaryOperation(Expression):
    def __init__(self, operator: str, operand: Expression):
        self.operator = operator
        self.operand = operand

class FunctionCall(Expression):
    def __init__(self, name: str, arguments: List[Expression]):
        self.name = name
        self.arguments = arguments

# Declarações
class VariableDeclaration(ASTNode):
    def __init__(self, name: str, var_type: str, value: Optional[Expression] = None):
        self.name = name
        self.var_type = var_type
        self.value = value

class ArrayDeclaration(ASTNode):
    def __init__(self, name: str, element_type: str, size: int):
        self.name = name
        self.element_type = element_type
        self.size = size

class Parameter(ASTNode):
    def __init__(self, name: str, param_type: str):
        self.name = name
        self.param_type = param_type

class ProcedureDeclaration(ASTNode):
    def __init__(self, name: str, parameters: List[Parameter], body: 'Block'):
        self.name = name
        self.parameters = parameters
        self.body = body

class FunctionDeclaration(ASTNode):
    def __init__(self, name: str, parameters: List[Parameter], return_type: str, body: 'Block'):
        self.name = name
        self.parameters = parameters
        self.return_type = return_type
        self.body = body

# Comandos
class Assignment(Statement):
    def __init__(self, target: Expression, value: Expression):
        self.target = target
        self.value = value

class IfStatement(Statement):
    def __init__(self, condition: Expression, then_stmt: Statement, else_stmt: Optional[Statement] = None):
        self.condition = condition
        self.then_stmt = then_stmt
        self.else_stmt = else_stmt

class WhileStatement(Statement):
    def __init__(self, condition: Expression, body: Statement):
        self.condition = condition
        self.body = body

class ForStatement(Statement):
    def __init__(self, variable: str, start: Expression, end: Expression, body: Statement):
        self.variable = variable
        self.start = start
        self.end = end
        self.body = body

class ProcedureCall(Statement):
    def __init__(self, name: str, arguments: List[Expression]):
        self.name = name
        self.arguments = arguments

class Block(Statement):
    def __init__(self, statements: List[Statement]):
        self.statements = statements

class ReadlnStatement(Statement):
    def __init__(self, targets: List[Expression]):
        self.targets = targets

class WritelnStatement(Statement):
    def __init__(self, expressions: List[Expression]):
        self.expressions = expressions

class ReturnStatement(Statement):
    def __init__(self, value: Optional[Expression] = None):
        self.value = value

# Programa principal
class Program(ASTNode):
    def __init__(self, name: str, declarations: List[ASTNode], body: Block):
        self.name = name
        self.declarations = declarations
        self.body = body
