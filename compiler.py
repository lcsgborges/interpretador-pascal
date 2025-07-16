"""
Compilador Pascal - Interface Principal
"""

import sys
import os
from typing import List
from src.compiler.lexer import Lexer, TokenType
from src.compiler.parser import Parser, ParseError
from src.compiler.interpreter import Interpreter, RuntimeError

class PascalCompiler:
    def __init__(self):
        self.lexer = None
        self.parser = None
        self.interpreter = None
    
    def compile_and_run(self, source_code: str, filename: str = "<string>"):
        """Compila e executa código Pascal"""
        try:
            print(f"Compilando {filename}...")
            
            # Análise Léxica
            print("Fase 1: Análise Léxica...")
            self.lexer = Lexer(source_code)
            tokens = self.lexer.tokenize()
            
            # Mostrar tokens em modo debug
            if '--debug' in sys.argv:
                print("Tokens encontrados:")
                for token in tokens:
                    if token.type != TokenType.EOF:
                        print(f"  {token.type.name}: {token.value} (linha {token.line})")
            
            # Análise Sintática
            print("Fase 2: Análise Sintática...")
            self.parser = Parser(tokens)
            ast = self.parser.parse()
            
            # Execução
            print("Fase 3: Execução...")
            print("-" * 40)
            
            self.interpreter = Interpreter()
            self.interpreter.interpret(ast)
            
            print("-" * 40)
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
    
    def compile_file(self, filename: str):
        """Compila e executa arquivo Pascal"""
        if not os.path.exists(filename):
            print(f"Erro: Arquivo '{filename}' não encontrado")
            sys.exit(1)
        
        if not filename.endswith('.pas'):
            print("Aviso: Arquivo não tem extensão .pas")
        
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                source_code = file.read()
            
            self.compile_and_run(source_code, filename)
            
        except FileNotFoundError:
            print(f"Erro: Arquivo '{filename}' não encontrado")
            sys.exit(1)
        except PermissionError:
            print(f"Erro: Sem permissão para ler o arquivo '{filename}'")
            sys.exit(1)
        except UnicodeDecodeError:
            print(f"Erro: Problema de codificação no arquivo '{filename}'")
            sys.exit(1)
    
    def interactive_mode(self):
        """Modo interativo para teste"""
        print("Compilador Pascal - Modo Interativo")
        print("Digite 'quit' para sair")
        print("-" * 40)
        
        while True:
            try:
                code = input(">>> ")
                if code.strip().lower() == 'quit':
                    break
                
                if code.strip():
                    self.compile_and_run(code, "<interactive>")
                    
            except KeyboardInterrupt:
                print("\nSaindo...")
                break
            except EOFError:
                print("\nSaindo...")
                break

def print_usage():
    """Mostra como usar o compilador"""
    print("Uso: python compiler.py [opções] [arquivo.pas]")
    print()
    print("Opções:")
    print("  -h, --help    Mostra esta ajuda")
    print("  -i, --interactive  Modo interativo")
    print("  --debug       Mostra tokens durante a compilação")
    print()
    print("Exemplos:")
    print("  python compiler.py exemplo.pas")
    print("  python compiler.py -i")
    print("  python compiler.py --debug programa.pas")

def main():
    if len(sys.argv) == 1:
        print_usage()
        return
    
    compiler = PascalCompiler()
    
    if '-h' in sys.argv or '--help' in sys.argv:
        print_usage()
        return
    
    if '-i' in sys.argv or '--interactive' in sys.argv:
        compiler.interactive_mode()
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
    
    compiler.compile_file(pascal_file)

if __name__ == "__main__":
    main()
