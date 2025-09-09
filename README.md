# Interpretador Pascal

## Introdução

Este projeto implementa um interpretador para um subconjunto da linguagem Pascal. O interpretador foi desenvolvido seguindo as etapas tradicionais de compilação: análise léxica, análise sintática e execução direta através de uma árvore sintática abstrata (AST).

### Funcionalidades Implementadas

O interpretador suporta as seguintes funcionalidades da linguagem Pascal:

- **Tipos de dados básicos**: integer, real, boolean, string
- **Operações aritméticas**: +, -, *, div, mod
- **Operações lógicas**: and, or, not
- **Operações de comparação**: =, <>, <, >, <=, >=
- **Estruturas de controle**: if-then-else, while-do, for-to-do
- **Arrays unidimensionais**: declaração e acesso por índices
- **Procedimentos**: com parâmetros e escopo local
- **Entrada/Saída**: readln e writeln com suporte a múltiplos parâmetros
- **Comentários**: suporte a comentários de linha (//) e bloco ({ })

### Conceitos Originais e Interessantes

**1. Sistema de Debugging Integrado**
- Modo ```--debug``` que exibe todos os tokens durante a análise léxica
- Informações detalhadas de linha e coluna para cada token
- Facilita a compreensão do processo de interpretação

**2. Interpretação Tree-Walking Otimizada**
- Execução direta da AST sem geração de código intermediário
- Ambiente de execução com gerenciamento de escopo aninhado
- Tratamento de exceções com mensagens informativas

**3. Sistema de Tipos Dinâmico com Validação**
- Verificação de tipos em tempo de execução
- Coerção automática entre tipos compatíveis
- Mensagens de erro precisas com localização

**4. Interface de Linha de Comando Avançada**
- Modo debug que exibe informações detalhadas de execução
- Suporte a múltiplos formatos de entrada
- Validação automática de extensões de arquivo

## Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior

### Instalação

```bash
git clone git@github.com:lcsgborges/trabalho-compiladores.git
cd trabalho-compiladores
```

## Como Usar

### Execução de Arquivo Pascal

```bash
# Sintaxe básica
python3 compiler.py arquivo.pas

# Com modo debug (mostra tokens)
python3 compiler.py --debug arquivo.pas

# Exemplos práticos
python3 compiler.py examples/hello.pas
python3 compiler.py examples/fibonacci.pas
python3 compiler.py examples/selection_sort.pas
```

### Usando o Makefile

```bash
# Executar todos os testes
make test

# Executar testes detalhados
make test-verbose

# Executar os 5 exemplos principais
make examples

# Executar arquivo específico
make run FILE=examples/hello.pas

# Limpar arquivos temporários
make clean

# Configuração inicial
make setup
```

## Exemplos de Programas Pascal

O projeto inclui 11 exemplos Pascal organizados por complexidade, localizados na pasta `examples/`:

### Lista Completa de Exemplos

**Básico:**
- hello.pas - Programa "Olá mundo" introdutório

**Intermediário:**
- fibonacci.pas - Sequência matemática com loops
- calculadora.pas - Operações aritméticas básicas
- controle_fluxo.pas - Estruturas if, while, for
- arrays.pas - Manipulação de vetores

**Avançado:**
- procedimentos.pas - Definição e uso de procedimentos
- procedimentos_simples.pas - Procedimentos com parâmetros
- exemplo_completo.pas - Sistema completo com arrays e estatísticas
- jogo_adivinhacao.pas - Jogo interativo
- selection_sort.pas - Algoritmo de ordenação por seleção
- bubble_sort.pas - Algoritmo de ordenação bubble sort

## Estrutura do Código

O projeto está organizado da seguinte forma:

```
trabalho-compiladores/
├── src/compiler/             # Código principal do interpretador
│   ├── lexer.py              # Analisador léxico
│   ├── parser.py             # Analisador sintático
│   ├── ast_nodes.py          # Definição dos nós da AST
│   ├── interpreter.py        # Interpretador tree-walking
│   └── __init__.py           # Módulo Python
├── examples/                 # 11 exemplos Pascal organizados por complexidade
├── tests/                    # Testes unitários
│   ├── test_lexer.py         # Testes do analisador léxico (6 testes)
│   ├── test_parser.py        # Testes do analisador sintático (6 testes)
│   ├── test_interpreter.py   # Testes do interpretador (7 testes)
│   └── run_tests.py          # Script para executar todos os testes
├── docs/                     # Documentação técnica
│   ├── architecture.md       # Arquitetura do sistema
│   └── syntax.md             # Sintaxe Pascal suportada
├── debug/                    # Pasta para arquivos de debugging
├── compiler.py               # Interface principal do interpretador
├── README.md                 # Este arquivo
├── Makefile                  # Automação de tarefas
└── requirements.txt          # Dependências (Python padrão apenas)
```

### Arquitetura do Sistema

**1. Analisador Léxico (lexer.py)**
- Converte código Pascal em tokens
- Identifica palavras-chave, operadores, literais e identificadores
- Remove comentários e espaços em branco
- Gera tokens com informação de posição para debug

**2. Analisador Sintático (parser.py)**
- Implementa parser recursive descent
- Constrói AST (Árvore Sintática Abstrata)
- Valida sintaxe seguindo gramática Pascal
- Detecta e reporta erros de sintaxe

**3. Nós da AST (ast_nodes.py)**
- Define classes para cada construção Pascal
- Hierarquia de classes representando elementos da linguagem
- Implementa padrão Visitor para travessia da árvore

**4. Interpretador (interpreter.py)**
- Executa programa através da travessia da AST
- Gerencia ambiente de execução e escopo de variáveis
- Implementa operações e estruturas de controle
- Trata erros de execução com mensagens informativas

**5. Interface Principal (compiler.py)**
- Interface de linha de comando
- Coordena as fases de análise e execução
- Implementa modo debug
- Trata exceções e fornece feedback ao usuário

## Documentação Técnica

A pasta `docs/` contém documentação técnica detalhada:

### docs/architecture.md
- Arquitetura completa do interpretador

### docs/syntax.md  
- Sintaxe Pascal completa suportada

## Testes Unitários

### Cobertura de Testes
- **Total**: 19 testes unitários

### Detalhamento por Módulo

**Análise Léxica (6 testes)**
- test_simple_tokens: Tokens básicos (program, begin, end, etc.)
- test_keywords: Palavras-chave da linguagem Pascal
- test_numbers: Números inteiros e reais
- test_strings: Literais string com aspas
- test_operators: Operadores aritméticos, relacionais e lógicos
- test_comments: Comentários de linha e bloco

**Análise Sintática (6 testes)**
- test_simple_program: Estrutura básica de programa Pascal
- test_variable_declaration: Declaração de variáveis com tipos
- test_assignment: Comandos de atribuição
- test_if_statement: Estruturas condicionais if-then-else
- test_while_statement: Loops while-do
- test_for_statement: Loops for-to-do

**Interpretação e Execução (7 testes)**
- test_simple_output: Comando writeln básico
- test_arithmetic: Operações aritméticas (+, -, *, div)
- test_boolean_operations: Operações lógicas (and, or, not)
- test_if_statement: Execução de condicionais
- test_while_loop: Execução de loops while
- test_for_loop: Execução de loops for
- test_arrays: Manipulação de arrays unidimensionais

### Execução dos Testes

```bash
# Todos os testes (19 testes)
python3 -m unittest tests.test_lexer tests.test_parser tests.test_interpreter -v

# Testes específicos por módulo
python3 -m unittest tests.test_lexer -v          # 6 testes de análise léxica
python3 -m unittest tests.test_parser -v         # 6 testes de análise sintática  
python3 -m unittest tests.test_interpreter -v    # 7 testes de interpretação

# Usando o Makefile
make test           # Execução normal
make test-verbose   # Execução detalhada
```

## Limitações Conhecidas

- Não suporte a funções que retornam valores (apenas procedimentos)
- Arrays apenas unidimensionais (sem matrizes)
- Sem gerenciamento dinâmico de memória
- Sem suporte a recursão complexa
- Strings não têm indexação direta
- Sem suporte a case/switch 

## Melhorias Futuras
- Implementar funções com valor de retorno
- Adicionar suporte a arrays multidimensionais
- Adicionar suporte a mais tipos de dados

## Referências

1. **Wirth, Niklaus** - "Pascal User Manual and Report": Referência principal para a especificação da linguagem Pascal.

2. **Aho, Alfred V. et al.** - "Compilers: Principles, Techniques, and Tools" (Dragon Book): Base teórica para implementação de compiladores e interpretadores.

3. **Grune, Dick et al.** - "Modern Compiler Design": Padrões de implementação de AST e técnicas de interpretação.

4. **Documentação Python 3.8+**: Implementação das estruturas de dados e algoritmos utilizados.

---
