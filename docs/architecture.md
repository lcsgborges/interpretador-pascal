# Arquitetura do Interpretador Pascal

## Componentes Principais

### 1. Lexer (Analisador Léxico)
- **Arquivo**: `src/compiler/lexer.py`
- **Responsabilidade**: Converter código fonte Pascal em tokens
- **Entrada**: String contendo código Pascal (.pas)
- **Saída**: Sequência de tokens classificados
- **Recursos**: Suporte a comentários, strings, números, operadores

### 2. Parser (Analisador Sintático)
- **Arquivo**: `src/compiler/parser.py`
- **Responsabilidade**: Converter tokens em AST (Árvore Sintática Abstrata)
- **Método**: Recursive Descent Parser
- **Entrada**: Lista de tokens do Lexer
- **Saída**: AST estruturada e validada

### 3. AST Nodes (Nós da AST)
- **Arquivo**: `src/compiler/ast_nodes.py`
- **Responsabilidade**: Definir estruturas de dados para representar construções Pascal
- **Implementação**: Classes Python para cada tipo de nó (Program, If, While, Assignment, etc.)
- **Padrão**: Visitor Pattern para travessia da árvore

### 4. Interpreter (Interpretador)
- **Arquivo**: `src/compiler/interpreter.py`
- **Responsabilidade**: Executar o programa através da travessia da AST
- **Tipo**: Tree-Walking Interpreter
- **Entrada**: AST válida do Parser
- **Saída**: Execução direta do programa

## Fluxo de Execução Detalhado

1. **Análise Léxica**: O código Pascal é tokenizado
   - Identifica palavras-chave, operadores, literais, identificadores
   - Remove comentários e espaços em branco
   - Gera tokens com posição para debug

2. **Análise Sintática**: Tokens são convertidos em AST
   - Validação sintática seguindo gramática Pascal
   - Construção de árvore hierárquica
   - Detecção de erros de sintaxe

3. **Interpretação**: AST é executada diretamente
   - Travessia em profundidade da árvore
   - Execução de operações e controle de fluxo
   - Gerenciamento de memória e escopo

## Estruturas de Dados

### Tokens
- **Estrutura**: `Token(type, value, line, column)`
- **Tipos**: KEYWORD, IDENTIFIER, NUMBER, STRING, OPERATOR, DELIMITER
- **Localização**: Para mensagens de erro precisas

### AST (Abstract Syntax Tree)
- **Hierarquia**: Classes Python para cada construção Pascal
- **Nó Raiz**: Sempre um `ProgramNode`
- **Composição**: Cada nó pode conter outros nós (árvore)
- **Método**: Visitor Pattern para travessia

### Environment (Ambiente de Execução)
- **Escopo**: Gerenciamento de variáveis locais/globais
- **Stack**: Controle de chamadas de procedimentos
- **Memória**: Arrays e estruturas de dados

## Funcionalidades Implementadas

### Suporte Completo
- Estrutura básica de programa Pascal
- Declaração e uso de variáveis (integer, real, boolean, string)
- Arrays unidimensionais com indexação
- Operações aritméticas (+, -, *, div, mod)
- Operações relacionais (=, <>, <, >, <=, >=)  
- Operações lógicas (and, or, not)
- Estruturas de controle (if-then-else, while-do, for-to-do)
- Entrada/saída (readln, writeln)
- Procedimentos com parâmetros
- Comentários de linha e bloco

### Limitações Conhecidas
- Não suporte a funções recursivas complexas
- Arrays apenas unidimensionais
- Sem suporte a records ou tipos customizados
- Sem gerenciamento dinâmico de memória

## Arquitetura de Testes

### Estrutura dos Testes
- **Lexer**: 6 testes cobrindo tokenização
- **Parser**: 6 testes cobrindo análise sintática  
- **Interpreter**: 7 testes cobrindo execução
- **Framework**: Python unittest