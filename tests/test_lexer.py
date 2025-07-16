"""
Testes unitários para o lexer
"""

import unittest
import sys
import os

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from compiler.lexer import Lexer, TokenType

class TestLexer(unittest.TestCase):
    
    def test_simple_tokens(self):
        """Testa tokens simples"""
        source = "program test;"
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.PROGRAM)
        self.assertEqual(tokens[1].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[1].value, "test")
        self.assertEqual(tokens[2].type, TokenType.SEMICOLON)
    
    def test_numbers(self):
        """Testa números inteiros e reais"""
        source = "123 45.67"
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.INTEGER)
        self.assertEqual(tokens[0].value, "123")
        self.assertEqual(tokens[1].type, TokenType.REAL)
        self.assertEqual(tokens[1].value, "45.67")
    
    def test_strings(self):
        """Testa strings"""
        source = "'hello world' \"test string\""
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.STRING)
        self.assertEqual(tokens[0].value, "hello world")
        self.assertEqual(tokens[1].type, TokenType.STRING)
        self.assertEqual(tokens[1].value, "test string")
    
    def test_operators(self):
        """Testa operadores"""
        source = "+ - * / := = <> < > <= >="
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        expected_types = [
            TokenType.PLUS, TokenType.MINUS, TokenType.MULTIPLY, 
            TokenType.DIVIDE, TokenType.ASSIGN, TokenType.EQUAL,
            TokenType.NOT_EQUAL, TokenType.LESS_THAN, TokenType.GREATER_THAN,
            TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL
        ]
        
        for i, expected_type in enumerate(expected_types):
            self.assertEqual(tokens[i].type, expected_type)
    
    def test_keywords(self):
        """Testa palavras-chave"""
        source = "begin end var if then else while do"
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        expected_types = [
            TokenType.BEGIN, TokenType.END, TokenType.VAR,
            TokenType.IF, TokenType.THEN, TokenType.ELSE,
            TokenType.WHILE, TokenType.DO
        ]
        
        for i, expected_type in enumerate(expected_types):
            self.assertEqual(tokens[i].type, expected_type)
    
    def test_comments(self):
        """Testa comentários"""
        source = "program test; { comentário } begin end."
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        # Comentários devem ser ignorados
        token_types = [token.type for token in tokens if token.type != TokenType.NEWLINE]
        expected_types = [
            TokenType.PROGRAM, TokenType.IDENTIFIER, TokenType.SEMICOLON,
            TokenType.BEGIN, TokenType.END, TokenType.DOT, TokenType.EOF
        ]
        
        self.assertEqual(token_types, expected_types)

if __name__ == '__main__':
    unittest.main()
