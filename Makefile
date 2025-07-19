.PHONY: help test test-verbose clean run examples setup 

help:
	@echo "Comandos disponíveis para o Interpretador Pascal:"
	@echo "  help          - Exibe esta ajuda"
	@echo "  test          - Executa todos os testes unitários (19 testes)"
	@echo "  test-verbose  - Executa testes com saída detalhada"
	@echo "  examples      - Executa todos os exemplos principais"
	@echo "  run FILE=<>   - Executa um arquivo Pascal específico"
	@echo "  clean         - Remove arquivos temporários e cache"
	@echo "  setup         - Configuração inicial do projeto"

# Executa todos os testes unitários
test:
	@echo "Executando bateria de testes completa..."
	python3 -m unittest tests.test_lexer tests.test_parser tests.test_interpreter -v

# Executa testes com saída mais detalhada
test-verbose:
	@echo "Executando testes detalhados por módulo..."
	@echo "--- Análise Léxica (6 testes) ---"
	python3 -m unittest tests.test_lexer -v
	@echo "--- Análise Sintática (6 testes) ---"
	python3 -m unittest tests.test_parser -v
	@echo "--- Interpretação (7 testes) ---"
	python3 -m unittest tests.test_interpreter -v

# Executa os 5 exemplos principais em sequência
examples:
	@echo "Executando exemplos principais do interpretador:"
	@echo "1. Hello World:"
	python3 compiler.py examples/hello.pas
	@echo "2. Fibonacci:"
	python3 compiler.py examples/fibonacci.pas
	@echo "3. Procedimentos:"
	python3 compiler.py examples/procedimentos_simples.pas
	@echo "4. Estruturas de Dados:"
	python3 compiler.py examples/exemplo_completo.pas
	@echo "5. Algoritmo de Ordenação:"
	python3 compiler.py examples/selection_sort.pas

# Executa arquivo específico
run:
ifdef FILE
	@echo "Executando $(FILE)..."
	python3 compiler.py $(FILE)
else
	@echo "Uso: make run FILE=caminho/arquivo.pas"
	@echo "Exemplo: make run FILE=examples/hello.pas"
endif

# Limpeza completa de arquivos temporários
clean:
	@echo "Limpando arquivos temporários..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -name ".DS_Store" -delete 2>/dev/null || true
	@echo "Limpeza concluída!"

# Configuração inicial do projeto
setup: clean install test
	@echo "Projeto configurado e validado com sucesso!"
	@echo "Estatísticas:"
	@echo "   - 19 testes unitários passando (100%)"
	@echo "   - Documentação completa em docs/"
	@echo "Pronto para uso! Execute 'make examples' para ver demonstrações."

# Informações do projeto
info:
	@echo "Interpretador Pascal - Informações do Projeto"
	@echo "Autores:"
	@echo "   - Lucas Guimarães Borges (222015159)"
	@echo "   - Maria Clara Alves de Sousa (221008329)"
	@echo "   - Davi Mesquita Sousa (222006650)"
	@echo "   - Daniel Fernandes Silva (222008459)"
	@echo "Universidade: Universidade de Brasília (UnB)"
	@echo "Disciplina: Compiladores"
	@echo "Tipo: Tree-Walking Interpreter para Pascal"
	@echo "Linguagem: Python 3.8+"
