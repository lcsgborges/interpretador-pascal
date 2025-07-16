# Makefile para o Compilador Pascal

.PHONY: help test clean run install dev

help:
	@echo "Comandos disponíveis:"
	@echo "  test      - Executar todos os testes"
	@echo "  clean     - Limpar arquivos temporários"
	@echo "  run       - Executar exemplo"
	@echo "  install   - Instalar dependências"
	@echo "  dev       - Configurar ambiente de desenvolvimento"

test:
	python3 tests/run_tests.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +

run:
	python3 compiler.py pascal_programs/hello.pas

install:
	pip3 install -r requirements.txt

dev:
	pip3 install -e .

lint:
	python3 -m flake8 src/ tests/

format:
	python3 -m black src/ tests/
