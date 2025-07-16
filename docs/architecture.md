# Arquitetura do Compilador Pascal

## Visão Geral

O compilador Pascal é implementado em Python seguindo a arquitetura tradicional de compiladores:

```
Código Pascal → Lexer → Parser → Interpretador → Saída
```

## Componentes

### 1. Lexer (Analisador Léxico)
- **Arquivo**: `src/compiler/lexer.py`
- **Responsabilidade**: Converter código fonte em tokens
- **Entrada**: String contendo código Pascal
- **Saída**: Lista de tokens

### 2. Parser (Analisador Sintático)
- **Arquivo**: `src/compiler/parser.py`
- **Responsabilidade**: Converter tokens em AST (Árvore Sintática Abstrata)
- **Entrada**: Lista de tokens
- **Saída**: AST

### 3. AST Nodes (Nós da AST)
- **Arquivo**: `src/compiler/ast_nodes.py`
- **Responsabilidade**: Definir estruturas de dados para a AST
- **Conteúdo**: Classes para representar construções da linguagem

### 4. Interpreter (Interpretador)
- **Arquivo**: `src/compiler/interpreter.py`
- **Responsabilidade**: Executar o programa a partir da AST
- **Entrada**: AST
- **Saída**: Execução do programa

## Fluxo de Execução

1. **Lexer**: Lê o código fonte e produz tokens
2. **Parser**: Analisa os tokens e constrói a AST
3. **Interpreter**: Percorre a AST e executa as instruções

## Estruturas de Dados

### Tokens
- Cada token tem tipo, valor, linha e coluna
- Tipos incluem: palavras-chave, identificadores, literais, operadores

### AST
- Hierarquia de classes representando construções da linguagem
- Nó raiz é sempre um `Program`
- Cada nó tem métodos para execução

### Environment
- Pilha de escopos para variáveis
- Suporte a funções e procedimentos
- Verificação de tipos básica
