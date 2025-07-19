"""
Analisador Sintático para o compilador Pascal.
Responsável por converter tokens em uma Árvore Sintática Abstrata (AST).
"""

from typing import List, Optional
from .lexer import Token, TokenType
from .ast_nodes import *

class ParseError(Exception):
    def __init__(self, message: str, token: Token):
        self.message = message
        self.token = token
        super().__init__(f"Erro sintático na linha {token.line}, coluna {token.column}: {message}")

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
    
    def current_token(self) -> Token:
        if self.current >= len(self.tokens):
            return self.tokens[-1]  # EOF token
        return self.tokens[self.current]
    
    def peek_token(self, offset: int = 1) -> Token:
        pos = self.current + offset
        if pos >= len(self.tokens):
            return self.tokens[-1]  # EOF token
        return self.tokens[pos]
    
    def advance(self) -> Token:
        token = self.current_token()
        if self.current < len(self.tokens) - 1:
            self.current += 1
        return token
    
    def match(self, *token_types: TokenType) -> bool:
        return self.current_token().type in token_types
    
    def consume(self, token_type: TokenType, message: str = None) -> Token:
        if self.current_token().type != token_type:
            if message is None:
                message = f"Esperado {token_type.name}, encontrado {self.current_token().type.name}"
            raise ParseError(message, self.current_token())
        
        token = self.current_token()
        self.advance()
        return token
    
    def skip_newlines(self):
        while self.match(TokenType.NEWLINE):
            self.advance()
    
    def parse(self) -> Program:
        return self.parse_program()
    
    def parse_program(self) -> Program:
        self.skip_newlines()
        self.consume(TokenType.PROGRAM, "Esperado 'program'")
        
        name_token = self.consume(TokenType.IDENTIFIER, "Esperado nome do programa")
        program_name = name_token.value
        
        self.consume(TokenType.SEMICOLON, "Esperado ';' após nome do programa")
        self.skip_newlines()
        
        declarations = []
        
        # Parse declarations
        while not self.match(TokenType.BEGIN, TokenType.EOF):
            if self.match(TokenType.VAR):
                declarations.extend(self.parse_variable_declarations())
            elif self.match(TokenType.PROCEDURE):
                declarations.append(self.parse_procedure_declaration())
            elif self.match(TokenType.FUNCTION):
                declarations.append(self.parse_function_declaration())
            else:
                self.advance()  # Skip unknown tokens
            self.skip_newlines()
        
        # Parse main body
        self.consume(TokenType.BEGIN, "Esperado 'begin'")
        self.skip_newlines()
        
        body = self.parse_block()
        
        self.consume(TokenType.DOT, "Esperado '.' no final do programa")
        
        return Program(program_name, declarations, body)
    
    def parse_variable_declarations(self) -> List[VariableDeclaration]:
        declarations = []
        self.consume(TokenType.VAR)
        self.skip_newlines()
        
        while not self.match(TokenType.BEGIN, TokenType.PROCEDURE, TokenType.FUNCTION, TokenType.EOF):
            if self.match(TokenType.IDENTIFIER):
                var_names = [self.consume(TokenType.IDENTIFIER).value]
                
                while self.match(TokenType.COMMA):
                    self.advance()
                    var_names.append(self.consume(TokenType.IDENTIFIER).value)
                
                self.consume(TokenType.COLON)
                
                if self.match(TokenType.ARRAY):
                    # Array declaration
                    self.advance()  # consume 'array'
                    self.consume(TokenType.LBRACKET)
                    
                    size_token = self.consume(TokenType.INTEGER)
                    size = int(size_token.value)
                    
                    self.consume(TokenType.RBRACKET)
                    self.consume(TokenType.OF)
                    
                    element_type = self.parse_type()
                    
                    for name in var_names:
                        declarations.append(ArrayDeclaration(name, element_type, size))
                else:
                    # Regular variable declaration
                    var_type = self.parse_type()
                    
                    for name in var_names:
                        declarations.append(VariableDeclaration(name, var_type))
                
                self.consume(TokenType.SEMICOLON)
                self.skip_newlines()
            else:
                break
        
        return declarations
    
    def parse_type(self) -> str:
        if self.match(TokenType.INTEGER_TYPE):
            self.advance()
            return 'integer'
        elif self.match(TokenType.REAL_TYPE):
            self.advance()
            return 'real'
        elif self.match(TokenType.BOOLEAN_TYPE):
            self.advance()
            return 'boolean'
        elif self.match(TokenType.STRING_TYPE):
            self.advance()
            return 'string'
        else:
            raise ParseError("Tipo esperado", self.current_token())
    
    def parse_procedure_declaration(self) -> ProcedureDeclaration:
        self.consume(TokenType.PROCEDURE)
        name = self.consume(TokenType.IDENTIFIER).value
        
        parameters = []
        if self.match(TokenType.LPAREN):
            parameters = self.parse_parameters()
        
        self.consume(TokenType.SEMICOLON)
        self.skip_newlines()
        
        # Parse local declarations
        local_declarations = []
        while self.match(TokenType.VAR):
            local_declarations.extend(self.parse_variable_declarations())
            self.skip_newlines()
        
        self.consume(TokenType.BEGIN)
        self.skip_newlines()
        
        body = self.parse_block()
        
        return ProcedureDeclaration(name, parameters, body)
    
    def parse_function_declaration(self) -> FunctionDeclaration:
        self.consume(TokenType.FUNCTION)
        name = self.consume(TokenType.IDENTIFIER).value
        
        parameters = []
        if self.match(TokenType.LPAREN):
            parameters = self.parse_parameters()
        
        self.consume(TokenType.COLON)
        return_type = self.parse_type()
        
        self.consume(TokenType.SEMICOLON)
        self.skip_newlines()
        
        # Parse local declarations
        local_declarations = []
        while self.match(TokenType.VAR):
            local_declarations.extend(self.parse_variable_declarations())
            self.skip_newlines()
        
        self.consume(TokenType.BEGIN)
        self.skip_newlines()
        
        body = self.parse_block()
        
        return FunctionDeclaration(name, parameters, return_type, body)
    
    def parse_parameters(self) -> List[Parameter]:
        parameters = []
        self.consume(TokenType.LPAREN)
        
        if not self.match(TokenType.RPAREN):
            while True:
                param_names = [self.consume(TokenType.IDENTIFIER).value]
                
                while self.match(TokenType.COMMA):
                    self.advance()
                    param_names.append(self.consume(TokenType.IDENTIFIER).value)
                
                self.consume(TokenType.COLON)
                param_type = self.parse_type()
                
                for name in param_names:
                    parameters.append(Parameter(name, param_type))
                
                if not self.match(TokenType.SEMICOLON):
                    break
                self.advance()
        
        self.consume(TokenType.RPAREN)
        return parameters
    
    def parse_block(self) -> Block:
        statements = []
        
        while not self.match(TokenType.END, TokenType.EOF):
            if self.match(TokenType.NEWLINE):
                self.advance()
                continue
            
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            else:
                # Se não conseguiu fazer parse do statement, avança para evitar loop infinito
                self.advance()
        
        self.consume(TokenType.END)
        return Block(statements)
    
    def parse_statement(self, require_semicolon=True) -> Optional[Statement]:
        self.skip_newlines()
        
        if self.match(TokenType.IDENTIFIER):
            return self.parse_assignment_or_call(require_semicolon)
        elif self.match(TokenType.IF):
            return self.parse_if_statement()
        elif self.match(TokenType.WHILE):
            return self.parse_while_statement()
        elif self.match(TokenType.FOR):
            return self.parse_for_statement()
        elif self.match(TokenType.READLN):
            return self.parse_readln_statement(require_semicolon)
        elif self.match(TokenType.WRITELN):
            return self.parse_writeln_statement(require_semicolon)
        elif self.match(TokenType.RETURN):
            return self.parse_return_statement(require_semicolon)
        elif self.match(TokenType.BEGIN):
            self.advance()
            self.skip_newlines()
            block = self.parse_block()
            return block
        elif self.match(TokenType.ELSE):
            # ELSE deve ser tratado apenas dentro de IF
            return None
        else:
            return None
    
    def parse_assignment_or_call(self, require_semicolon=True) -> Statement:
        name = self.consume(TokenType.IDENTIFIER).value
        
        if self.match(TokenType.ASSIGN):
            # Assignment
            self.advance()
            value = self.parse_expression()
            if require_semicolon:
                self.consume(TokenType.SEMICOLON)
            return Assignment(Variable(name), value)
        elif self.match(TokenType.LBRACKET):
            # Array assignment
            self.advance()
            index = self.parse_expression()
            self.consume(TokenType.RBRACKET)
            self.consume(TokenType.ASSIGN)
            value = self.parse_expression()
            if require_semicolon:
                self.consume(TokenType.SEMICOLON)
            return Assignment(ArrayAccess(Variable(name), index), value)
        elif self.match(TokenType.LPAREN):
            # Procedure call
            self.advance()
            arguments = []
            
            if not self.match(TokenType.RPAREN):
                arguments.append(self.parse_expression())
                while self.match(TokenType.COMMA):
                    self.advance()
                    arguments.append(self.parse_expression())
            
            self.consume(TokenType.RPAREN)
            if require_semicolon:
                self.consume(TokenType.SEMICOLON)
            return ProcedureCall(name, arguments)
        else:
            # Simple procedure call without parameters
            if require_semicolon:
                self.consume(TokenType.SEMICOLON)
            return ProcedureCall(name, [])
    
    def parse_if_statement(self) -> IfStatement:
        self.consume(TokenType.IF)
        condition = self.parse_expression()
        self.consume(TokenType.THEN)
        self.skip_newlines()
        
        # Verificar se o próximo token é BEGIN
        if self.match(TokenType.BEGIN):
            # Se for BEGIN, parse normalmente (com semicolons)
            then_stmt = self.parse_statement()
        else:
            # Se não for BEGIN, não requer semicolon antes do ELSE
            then_stmt = self.parse_statement(require_semicolon=False)
        
        # Debug: verificar token atual
        # print(f"DEBUG: Após then_stmt, token atual: {self.current_token()}")
        
        self.skip_newlines()  
        
        else_stmt = None
        if self.match(TokenType.ELSE):
            self.advance()
            self.skip_newlines()
            
            # Verificar se o próximo token é BEGIN
            if self.match(TokenType.BEGIN):
                # Se for BEGIN, parse normalmente (com semicolons)
                else_stmt = self.parse_statement()
            else:
                # Se não for BEGIN, não requer semicolon
                else_stmt = self.parse_statement(require_semicolon=False)
        
        return IfStatement(condition, then_stmt, else_stmt)
    
    def parse_while_statement(self) -> WhileStatement:
        self.consume(TokenType.WHILE)
        condition = self.parse_expression()
        self.consume(TokenType.DO)
        self.skip_newlines()
        
        body = self.parse_statement()
        return WhileStatement(condition, body)
    
    def parse_for_statement(self) -> ForStatement:
        self.consume(TokenType.FOR)
        variable = self.consume(TokenType.IDENTIFIER).value
        self.consume(TokenType.ASSIGN)
        start = self.parse_expression()
        self.consume(TokenType.TO)
        end = self.parse_expression()
        self.consume(TokenType.DO)
        self.skip_newlines()
        
        body = self.parse_statement()
        return ForStatement(variable, start, end, body)
    
    def parse_readln_statement(self, require_semicolon=True) -> ReadlnStatement:
        self.consume(TokenType.READLN)
        targets = []
        
        if self.match(TokenType.LPAREN):
            self.advance()
            targets.append(self.parse_primary_expression())
            
            while self.match(TokenType.COMMA):
                self.advance()
                targets.append(self.parse_primary_expression())
            
            self.consume(TokenType.RPAREN)
        
        if require_semicolon:
            self.consume(TokenType.SEMICOLON)
        
        return ReadlnStatement(targets)
    
    def parse_writeln_statement(self, require_semicolon=True) -> WritelnStatement:
        self.consume(TokenType.WRITELN)
        expressions = []
        
        if self.match(TokenType.LPAREN):
            self.advance()
            if not self.match(TokenType.RPAREN):
                expressions.append(self.parse_expression())
                
                while self.match(TokenType.COMMA):
                    self.advance()
                    expressions.append(self.parse_expression())
            
            self.consume(TokenType.RPAREN)
        
        # Só consome ponto e vírgula se requerido
        if require_semicolon:
            self.consume(TokenType.SEMICOLON)
        
        return WritelnStatement(expressions)
    
    def parse_return_statement(self, require_semicolon=True) -> ReturnStatement:
        self.consume(TokenType.RETURN)
        
        value = None
        if not self.match(TokenType.SEMICOLON) and not self.match(TokenType.NEWLINE, TokenType.END, TokenType.ELSE):
            value = self.parse_expression()
        
        if require_semicolon:
            self.consume(TokenType.SEMICOLON)
        
        return ReturnStatement(value)
    
    def parse_expression(self) -> Expression:
        return self.parse_or_expression()
    
    def parse_or_expression(self) -> Expression:
        expr = self.parse_and_expression()
        
        while self.match(TokenType.OR):
            operator = self.advance().value
            right = self.parse_and_expression()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def parse_and_expression(self) -> Expression:
        expr = self.parse_equality_expression()
        
        while self.match(TokenType.AND):
            operator = self.advance().value
            right = self.parse_equality_expression()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def parse_equality_expression(self) -> Expression:
        expr = self.parse_relational_expression()
        
        while self.match(TokenType.EQUAL, TokenType.NOT_EQUAL):
            operator = self.advance().value
            right = self.parse_relational_expression()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def parse_relational_expression(self) -> Expression:
        expr = self.parse_additive_expression()
        
        while self.match(TokenType.LESS_THAN, TokenType.GREATER_THAN, 
                         TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL):
            operator = self.advance().value
            right = self.parse_additive_expression()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def parse_additive_expression(self) -> Expression:
        expr = self.parse_multiplicative_expression()
        
        while self.match(TokenType.PLUS, TokenType.MINUS):
            operator = self.advance().value
            right = self.parse_multiplicative_expression()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def parse_multiplicative_expression(self) -> Expression:
        expr = self.parse_unary_expression()
        
        while self.match(TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.DIV, TokenType.MOD):
            operator = self.advance().value
            right = self.parse_unary_expression()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def parse_unary_expression(self) -> Expression:
        if self.match(TokenType.NOT, TokenType.PLUS, TokenType.MINUS):
            operator = self.advance().value
            operand = self.parse_unary_expression()
            return UnaryOperation(operator, operand)
        
        return self.parse_primary_expression()
    
    def parse_primary_expression(self) -> Expression:
        if self.match(TokenType.INTEGER):
            value = int(self.advance().value)
            return NumberLiteral(value)
        elif self.match(TokenType.REAL):
            value = float(self.advance().value)
            return NumberLiteral(value)
        elif self.match(TokenType.STRING):
            value = self.advance().value
            return StringLiteral(value)
        elif self.match(TokenType.TRUE):
            self.advance()
            return BooleanLiteral(True)
        elif self.match(TokenType.FALSE):
            self.advance()
            return BooleanLiteral(False)
        elif self.match(TokenType.IDENTIFIER):
            name = self.advance().value
            
            if self.match(TokenType.LPAREN):
                # Function call
                self.advance()
                arguments = []
                
                if not self.match(TokenType.RPAREN):
                    arguments.append(self.parse_expression())
                    while self.match(TokenType.COMMA):
                        self.advance()
                        arguments.append(self.parse_expression())
                
                self.consume(TokenType.RPAREN)
                return FunctionCall(name, arguments)
            elif self.match(TokenType.LBRACKET):
                # Array access
                self.advance()
                index = self.parse_expression()
                self.consume(TokenType.RBRACKET)
                return ArrayAccess(Variable(name), index)
            else:
                # Variable
                return Variable(name)
        elif self.match(TokenType.LPAREN):
            self.advance()
            expr = self.parse_expression()
            self.consume(TokenType.RPAREN)
            return expr
        else:
            raise ParseError("Expressão esperada", self.current_token())
