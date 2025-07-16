"""
Testes unitários para o interpretador
"""

import unittest
import sys
import os

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from compiler.lexer import Lexer
from compiler.parser import Parser
from compiler.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):
    
    def interpret_source(self, source):
        """Helper para interpretar código"""
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        interpreter = Interpreter()
        interpreter.interpret(ast)
        return interpreter.get_output()
    
    def test_simple_output(self):
        """Testa saída simples"""
        source = """
        program test;
        begin
            writeln('Hello World');
        end.
        """
        
        output = self.interpret_source(source)
        self.assertEqual(output, ['Hello World'])
    
    def test_arithmetic(self):
        """Testa operações aritméticas"""
        source = """
        program test;
        var x, y: integer;
        begin
            x := 10;
            y := 5;
            writeln(x + y);
            writeln(x - y);
            writeln(x * y);
            writeln(x div y);
        end.
        """
        
        output = self.interpret_source(source)
        self.assertEqual(output, ['15', '5', '50', '2'])
    
    def test_boolean_operations(self):
        """Testa operações booleanas"""
        source = """
        program test;
        var a, b: boolean;
        begin
            a := true;
            b := false;
            writeln(a and b);
            writeln(a or b);
            writeln(not a);
        end.
        """
        
        output = self.interpret_source(source)
        self.assertEqual(output, ['False', 'True', 'False'])
    
    def test_if_statement(self):
        """Testa comando if"""
        source = """
        program test;
        var x: integer;
        begin
            x := 10;
            if x > 5 then
                writeln('maior')
            else
                writeln('menor');
        end.
        """
        
        output = self.interpret_source(source)
        self.assertEqual(output, ['maior'])
    
    def test_while_loop(self):
        """Testa loop while"""
        source = """
        program test;
        var i: integer;
        begin
            i := 1;
            while i <= 3 do
            begin
                writeln(i);
                i := i + 1;
            end;
        end.
        """
        
        output = self.interpret_source(source)
        self.assertEqual(output, ['1', '2', '3'])
    
    def test_for_loop(self):
        """Testa loop for"""
        source = """
        program test;
        var i: integer;
        begin
            for i := 1 to 3 do
                writeln(i);
        end.
        """
        
        output = self.interpret_source(source)
        self.assertEqual(output, ['1', '2', '3'])
    
    def test_arrays(self):
        """Testa arrays"""
        source = """
        program test;
        var arr: array[3] of integer;
        var i: integer;
        begin
            arr[0] := 10;
            arr[1] := 20;
            arr[2] := 30;
            
            for i := 0 to 2 do
                writeln(arr[i]);
        end.
        """
        
        output = self.interpret_source(source)
        self.assertEqual(output, ['10', '20', '30'])

if __name__ == '__main__':
    unittest.main()
