# Compilador Pascal em Python

Este é um compilador/interpretador de Pascal implementado em Python para a disciplina de Compiladores I.

## Estrutura do Projeto

```
trabalho-compiladores/
├── src/                    # Código fonte
│   └── compiler/           # Módulos do compilador
│       ├── __init__.py
│       ├── lexer.py        # Analisador léxico
│       ├── parser.py       # Analisador sintático
│       ├── interpreter.py  # Interpretador
│       └── ast_nodes.py    # Nós da AST
├── tests/                  # Testes unitários
│   ├── __init__.py
│   ├── test_lexer.py
│   ├── test_parser.py
│   ├── test_interpreter.py
│   └── run_tests.py
├── pascal_programs/        # Programas Pascal de exemplo
├── debug/                  # Arquivos para debug
├── docs/                   # Documentação
│   ├── architecture.md
│   └── syntax.md
├── compiler.py             # Interface principal
├── Makefile               # Comandos úteis
└── README.md              # Este arquivo
```

## Como usar

### Instalação

```bash
# Clonar o repositório
git clone <git@github.com:lcsgborges/trabalho-compiladores.git>
cd trabalho-compiladores
```

### Execução

```bash
# Compilar e executar um programa Pascal
python3 compiler.py pascal_programs/hello.pas

# Modo interativo
python3 compiler.py -i

# Modo debug (mostra tokens)
python3 compiler.py --debug pascal_programs/hello.pas

# Ajuda
python3 compiler.py --help
```

### Usando Makefile

```bash
# Executar exemplo
make run

# Executar testes
make test

# Limpar arquivos temporários
make clean
```

## Funcionalidades Suportadas

### Tipos de Dados
- `integer` - números inteiros
- `real` - números reais
- `boolean` - verdadeiro/falso
- `string` - texto
- `array` - arrays unidimensionais

### Operações
- **Aritméticas**: `+`, `-`, `*`, `/`, `div`, `mod`
- **Relacionais**: `=`, `<>`, `<`, `>`, `<=`, `>=`
- **Lógicas**: `and`, `or`, `not`

### Estruturas de Controle
- `if-then-else` - condicionais
- `while-do` - loops condicionais
- `for-to-do` - loops com contador

### Subprogramas
- `procedure` - procedimentos
- `function` - funções com valor de retorno

### Entrada/Saída
- `readln()` - leitura de dados
- `writeln()` - escrita de dados

## Exemplos

### Hello World
```pascal
program HelloWorld;
begin
    writeln('Olá, mundo!');
end.
```

### Calculadora
```pascal
program Calculadora;
var
    a, b: integer;
begin
    writeln('Digite dois números:');
    readln(a, b);
    writeln('Soma: ', a + b);
end.
```

### Função Recursiva
```pascal
program Fatorial;
var
    n: integer;

function fatorial(x: integer): integer;
begin
    if x <= 1 then
        return 1
    else
        return x * fatorial(x - 1);
end;

begin
    writeln('Digite um número:');
    readln(n);
    writeln('Fatorial: ', fatorial(n));
end.
```

## Testes

```bash
# Executar todos os testes
python3 tests/run_tests.py

# Ou usando make
make test

# Executar teste específico
python3 -m unittest tests.test_lexer
```

## Documentação

- [Arquitetura](docs/architecture.md) - Visão geral da arquitetura
- [Sintaxe](docs/syntax.md) - Sintaxe suportada

## Debug

Para debugar problemas, use:

```bash
# Modo debug - mostra tokens
python3 compiler.py --debug programa.pas

# Salvar arquivos de debug na pasta debug/
```

## Desenvolvimento

### Estrutura do Compilador

1. **Lexer** (`src/compiler/lexer.py`)
   - Converte código fonte em tokens
   - Reconhece palavras-chave, identificadores, literais, operadores

2. **Parser** (`src/compiler/parser.py`)
   - Converte tokens em AST (Árvore Sintática Abstrata)
   - Implementa gramática Pascal

3. **Interpreter** (`src/compiler/interpreter.py`)
   - Executa o programa a partir da AST
   - Gerencia escopos e variáveis

4. **AST Nodes** (`src/compiler/ast_nodes.py`)
   - Define estruturas de dados para a AST
   - Representa construções da linguagem

## Limitações

- Apenas arrays unidimensionais
- Sem verificação de tipos avançada
- Sem otimizações
- Sem geração de código objeto

## Autores

- Lucas Guimarães Borges (222015159)
- Maria Clara Alves de Sousa (221008329)
