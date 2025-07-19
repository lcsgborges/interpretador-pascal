"""
Interpretador Pascal - Interface Principal
"""

import sys
import os
from src.compiler.lexer import Lexer, TokenType
from src.compiler.parser import Parser, ParseError
from src.compiler.interpreter import Interpreter, RuntimeError

class PascalInterpreter:
    """
    Interpretador Pascal implementado em Python.
    
    Utiliza arquitetura tree-walking interpreter:
    Código Pascal → Lexer → Parser → AST → Interpreter → Execução
    """
    
    def __init__(self):
        self.lexer = None
        self.parser = None
        self.interpreter = None
    
    def interpret(self, source_code: str, filename: str = "<string>"):
        """Interpreta e executa código Pascal"""
        try:
            print(f"Interpretando {filename}...")
            
            print("Fase 1: Análise Léxica...")
            self.lexer = Lexer(source_code)
            tokens = self.lexer.tokenize()
            
            if '--debug' in sys.argv:
                print("Tokens encontrados:")
                for token in tokens:
                    if token.type != TokenType.EOF:
                        print(f"  {token.type.name}: {token.value} (linha {token.line})")
            
            print("Fase 2: Análise Sintática...")
            self.parser = Parser(tokens)
            ast = self.parser.parse()
            
            print("Fase 3: Interpretação e Execução...")
            print("-" * 50)
            
            self.interpreter = Interpreter()
            self.interpreter.interpret(ast)
            
            print("-" * 50)
            print("Programa executado com sucesso!")
            
        except ParseError as e:
            print(f"Erro de sintaxe: {e}")
            sys.exit(1)
        except RuntimeError as e:
            print(f"Erro de execução: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            sys.exit(1)
    
    def interpret_file(self, filename: str):
        """Interpreta e executa arquivo Pascal"""
        if not os.path.exists(filename):
            print(f"Erro: Arquivo '{filename}' não encontrado")
            sys.exit(1)
        
        if not filename.endswith('.pas'):
            print("Aviso: Arquivo não tem extensão .pas")
        
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                source_code = file.read()
            
            self.interpret(source_code, filename)
            
        except FileNotFoundError:
            print(f"Erro: Arquivo '{filename}' não encontrado")
            sys.exit(1)
        except PermissionError:
            print(f"Erro: Sem permissão para ler o arquivo '{filename}'")
            sys.exit(1)
        except UnicodeDecodeError:
            print(f"Erro: Problema de codificação no arquivo '{filename}'")
            sys.exit(1)

def print_usage():
    """Mostra informações de uso do interpretador"""
    print("Interpretador Pascal")
    print()
    print("Uso: python3 compiler.py [opções] [arquivo.pas]")
    print()
    print("Opções:")
    print("  -h, --help       Mostra esta ajuda")
    print("  --debug          Mostra tokens durante interpretação")
    print()
    print("Exemplos:")
    print("  python3 compiler.py examples/hello.pas")
    print("  python3 compiler.py --debug examples/exemplo_completo.pas")
    print()
    print("Exemplos disponíveis em examples/:")
    print("  hello.pas, fibonacci.pas, procedimentos_simples.pas,")
    print("  exemplo_completo.pas, selection_sort.pas, bubble_sort.pas")

def main():
    """Função principal do interpretador Pascal"""
    if len(sys.argv) == 1:
        print_usage()
        return
    
    interpreter = PascalInterpreter()
    
    if '-h' in sys.argv or '--help' in sys.argv:
        print_usage()
        return
    
    # Encontrar arquivo Pascal
    pascal_file = None
    for arg in sys.argv[1:]:
        if not arg.startswith('-'):
            pascal_file = arg
            break
    
    if pascal_file is None:
        print("Erro: Nenhum arquivo especificado")
        print_usage()
        sys.exit(1)
    
    interpreter.interpret_file(pascal_file)

if __name__ == "__main__":
    main()
