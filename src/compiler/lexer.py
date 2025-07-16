"""
Analisador Léxico para o compilador Pascal.
Responsável por converter o código fonte em tokens.
"""

import re
from enum import Enum, auto
from typing import List, Optional, NamedTuple

class TokenType(Enum):
    # Literais
    INTEGER = auto()
    REAL = auto()
    STRING = auto()
    BOOLEAN = auto()
    
    # Identificadores
    IDENTIFIER = auto()
    
    # Palavras-chave
    PROGRAM = auto()
    BEGIN = auto()
    END = auto()
    VAR = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    WHILE = auto()
    DO = auto()
    FOR = auto()
    TO = auto()
    PROCEDURE = auto()
    FUNCTION = auto()
    ARRAY = auto()
    OF = auto()
    TRUE = auto()
    FALSE = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    DIV = auto()
    MOD = auto()
    READLN = auto()
    WRITELN = auto()
    RETURN = auto()
    
    # Tipos
    INTEGER_TYPE = auto()
    REAL_TYPE = auto()
    BOOLEAN_TYPE = auto()
    STRING_TYPE = auto()
    
    # Operadores
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    ASSIGN = auto()
    EQUAL = auto()
    NOT_EQUAL = auto()
    LESS_THAN = auto()
    GREATER_THAN = auto()
    LESS_EQUAL = auto()
    GREATER_EQUAL = auto()
    
    # Delimitadores
    SEMICOLON = auto()
    COMMA = auto()
    DOT = auto()
    COLON = auto()
    LPAREN = auto()
    RPAREN = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    
    # Especiais
    EOF = auto()
    NEWLINE = auto()

class Token(NamedTuple):
    type: TokenType
    value: str
    line: int
    column: int

class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []
        
        # Palavras-chave
        self.keywords = {
            'program': TokenType.PROGRAM,
            'begin': TokenType.BEGIN,
            'end': TokenType.END,
            'var': TokenType.VAR,
            'if': TokenType.IF,
            'then': TokenType.THEN,
            'else': TokenType.ELSE,
            'while': TokenType.WHILE,
            'do': TokenType.DO,
            'for': TokenType.FOR,
            'to': TokenType.TO,
            'procedure': TokenType.PROCEDURE,
            'function': TokenType.FUNCTION,
            'array': TokenType.ARRAY,
            'of': TokenType.OF,
            'true': TokenType.TRUE,
            'false': TokenType.FALSE,
            'and': TokenType.AND,
            'or': TokenType.OR,
            'not': TokenType.NOT,
            'div': TokenType.DIV,
            'mod': TokenType.MOD,
            'readln': TokenType.READLN,
            'writeln': TokenType.WRITELN,
            'return': TokenType.RETURN,
            'integer': TokenType.INTEGER_TYPE,
            'real': TokenType.REAL_TYPE,
            'boolean': TokenType.BOOLEAN_TYPE,
            'string': TokenType.STRING_TYPE,
        }
    
    def current_char(self) -> Optional[str]:
        if self.position >= len(self.source):
            return None
        return self.source[self.position]
    
    def peek_char(self, offset: int = 1) -> Optional[str]:
        peek_pos = self.position + offset
        if peek_pos >= len(self.source):
            return None
        return self.source[peek_pos]
    
    def advance(self):
        if self.position < len(self.source):
            if self.source[self.position] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.position += 1
    
    def skip_whitespace(self):
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def skip_comment(self):
        if self.current_char() == '{':
            self.advance()
            while self.current_char() and self.current_char() != '}':
                self.advance()
            if self.current_char() == '}':
                self.advance()
        elif self.current_char() == '/' and self.peek_char() == '/':
            self.advance()
            self.advance()
            while self.current_char() and self.current_char() != '\n':
                self.advance()
    
    def read_number(self) -> Token:
        start_pos = (self.line, self.column)
        value = ''
        
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            value += self.current_char()
            self.advance()
        
        if '.' in value:
            return Token(TokenType.REAL, value, start_pos[0], start_pos[1])
        else:
            return Token(TokenType.INTEGER, value, start_pos[0], start_pos[1])
    
    def read_string(self) -> Token:
        start_pos = (self.line, self.column)
        value = ''
        quote_char = self.current_char()
        self.advance()  # Skip opening quote
        
        while self.current_char() and self.current_char() != quote_char:
            if self.current_char() == '\\':
                self.advance()
                if self.current_char() == 'n':
                    value += '\n'
                elif self.current_char() == 't':
                    value += '\t'
                elif self.current_char() == 'r':
                    value += '\r'
                elif self.current_char() == '\\':
                    value += '\\'
                elif self.current_char() == quote_char:
                    value += quote_char
                else:
                    value += self.current_char()
                self.advance()
            else:
                value += self.current_char()
                self.advance()
        
        if self.current_char() == quote_char:
            self.advance()  # Skip closing quote
        
        return Token(TokenType.STRING, value, start_pos[0], start_pos[1])
    
    def read_identifier(self) -> Token:
        start_pos = (self.line, self.column)
        value = ''
        
        while (self.current_char() and 
               (self.current_char().isalnum() or self.current_char() == '_')):
            value += self.current_char()
            self.advance()
        
        # Verificar se é uma palavra-chave
        token_type = self.keywords.get(value.lower(), TokenType.IDENTIFIER)
        return Token(token_type, value, start_pos[0], start_pos[1])
    
    def tokenize(self) -> List[Token]:
        while self.current_char():
            self.skip_whitespace()
            
            if not self.current_char():
                break
            
            # Comentários
            if self.current_char() == '{' or (self.current_char() == '/' and self.peek_char() == '/'):
                self.skip_comment()
                continue
            
            # Nova linha
            if self.current_char() == '\n':
                token = Token(TokenType.NEWLINE, '\n', self.line, self.column)
                self.tokens.append(token)
                self.advance()
                continue
            
            # Números
            if self.current_char().isdigit():
                self.tokens.append(self.read_number())
                continue
            
            # Strings
            if self.current_char() in '"\'':
                self.tokens.append(self.read_string())
                continue
            
            # Identificadores e palavras-chave
            if self.current_char().isalpha() or self.current_char() == '_':
                self.tokens.append(self.read_identifier())
                continue
            
            # Operadores e delimitadores
            char = self.current_char()
            pos = (self.line, self.column)
            
            if char == '+':
                self.tokens.append(Token(TokenType.PLUS, char, pos[0], pos[1]))
            elif char == '-':
                self.tokens.append(Token(TokenType.MINUS, char, pos[0], pos[1]))
            elif char == '*':
                self.tokens.append(Token(TokenType.MULTIPLY, char, pos[0], pos[1]))
            elif char == '/':
                self.tokens.append(Token(TokenType.DIVIDE, char, pos[0], pos[1]))
            elif char == '=':
                self.tokens.append(Token(TokenType.EQUAL, char, pos[0], pos[1]))
            elif char == '<':
                if self.peek_char() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.LESS_EQUAL, '<=', pos[0], pos[1]))
                elif self.peek_char() == '>':
                    self.advance()
                    self.tokens.append(Token(TokenType.NOT_EQUAL, '<>', pos[0], pos[1]))
                else:
                    self.tokens.append(Token(TokenType.LESS_THAN, char, pos[0], pos[1]))
            elif char == '>':
                if self.peek_char() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.GREATER_EQUAL, '>=', pos[0], pos[1]))
                else:
                    self.tokens.append(Token(TokenType.GREATER_THAN, char, pos[0], pos[1]))
            elif char == ':':
                if self.peek_char() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.ASSIGN, ':=', pos[0], pos[1]))
                else:
                    self.tokens.append(Token(TokenType.COLON, char, pos[0], pos[1]))
            elif char == ';':
                self.tokens.append(Token(TokenType.SEMICOLON, char, pos[0], pos[1]))
            elif char == ',':
                self.tokens.append(Token(TokenType.COMMA, char, pos[0], pos[1]))
            elif char == '.':
                self.tokens.append(Token(TokenType.DOT, char, pos[0], pos[1]))
            elif char == '(':
                self.tokens.append(Token(TokenType.LPAREN, char, pos[0], pos[1]))
            elif char == ')':
                self.tokens.append(Token(TokenType.RPAREN, char, pos[0], pos[1]))
            elif char == '[':
                self.tokens.append(Token(TokenType.LBRACKET, char, pos[0], pos[1]))
            elif char == ']':
                self.tokens.append(Token(TokenType.RBRACKET, char, pos[0], pos[1]))
            else:
                raise SyntaxError(f"Caractere inesperado '{char}' na linha {self.line}, coluna {self.column}")
            
            self.advance()
        
        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens
