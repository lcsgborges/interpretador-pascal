"""
Testes unitários para o parser
"""

import unittest
import sys
import os

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from compiler.lexer import Lexer
from compiler.parser import Parser
from compiler.ast_nodes import *

class TestParser(unittest.TestCase):
    
    def parse_source(self, source):
        """Helper para parsing"""
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        return parser.parse()
    
    def test_simple_program(self):
        """Testa programa simples"""
        source = """
        program test;
        begin
        end.
        """
        
        ast = self.parse_source(source)
        self.assertIsInstance(ast, Program)
        self.assertEqual(ast.name, "test")
        self.assertIsInstance(ast.body, Block)
    
    def test_variable_declaration(self):
        """Testa declaração de variáveis"""
        source = """
        program test;
        var
            x, y: integer;
            z: real;
        begin
        end.
        """
        
        ast = self.parse_source(source)
        self.assertEqual(len(ast.declarations), 3)
        
        # Primeira declaração: x: integer
        self.assertIsInstance(ast.declarations[0], VariableDeclaration)
        self.assertEqual(ast.declarations[0].name, "x")
        self.assertEqual(ast.declarations[0].var_type, "integer")
        
        # Segunda declaração: y: integer
        self.assertIsInstance(ast.declarations[1], VariableDeclaration)
        self.assertEqual(ast.declarations[1].name, "y")
        self.assertEqual(ast.declarations[1].var_type, "integer")
        
        # Terceira declaração: z: real
        self.assertIsInstance(ast.declarations[2], VariableDeclaration)
        self.assertEqual(ast.declarations[2].name, "z")
        self.assertEqual(ast.declarations[2].var_type, "real")
    
    def test_assignment(self):
        """Testa atribuição"""
        source = """
        program test;
        var x: integer;
        begin
            x := 42;
        end.
        """
        
        ast = self.parse_source(source)
        self.assertEqual(len(ast.body.statements), 1)
        
        stmt = ast.body.statements[0]
        self.assertIsInstance(stmt, Assignment)
        self.assertIsInstance(stmt.target, Variable)
        self.assertEqual(stmt.target.name, "x")
        self.assertIsInstance(stmt.value, NumberLiteral)
        self.assertEqual(stmt.value.value, 42)
    
    def test_if_statement(self):
        """Testa comando if"""
        source = """
        program test;
        var x: integer;
        begin
            if x > 0 then
                x := 1
            else
                x := 0;
        end.
        """
        
        ast = self.parse_source(source)
        stmt = ast.body.statements[0]
        
        self.assertIsInstance(stmt, IfStatement)
        self.assertIsInstance(stmt.condition, BinaryOperation)
        self.assertIsInstance(stmt.then_stmt, Assignment)
        self.assertIsInstance(stmt.else_stmt, Assignment)
    
    def test_while_statement(self):
        """Testa comando while"""
        source = """
        program test;
        var x: integer;
        begin
            while x > 0 do
                x := x - 1;
        end.
        """
        
        ast = self.parse_source(source)
        stmt = ast.body.statements[0]
        
        self.assertIsInstance(stmt, WhileStatement)
        self.assertIsInstance(stmt.condition, BinaryOperation)
        self.assertIsInstance(stmt.body, Assignment)
    
    def test_for_statement(self):
        """Testa comando for"""
        source = """
        program test;
        var i: integer;
        begin
            for i := 1 to 10 do
                writeln(i);
        end.
        """
        
        ast = self.parse_source(source)
        stmt = ast.body.statements[0]
        
        self.assertIsInstance(stmt, ForStatement)
        self.assertEqual(stmt.variable, "i")
        self.assertIsInstance(stmt.start, NumberLiteral)
        self.assertIsInstance(stmt.end, NumberLiteral)
        self.assertIsInstance(stmt.body, WritelnStatement)

if __name__ == '__main__':
    unittest.main()
