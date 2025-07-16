# Sintaxe Suportada

## Estrutura Básica

```pascal
program NomePrograma;
{ declarações }
begin
    { comandos }
end.
```

## Declarações

### Variáveis
```pascal
var
    x, y: integer;
    z: real;
    nome: string;
    ativo: boolean;
```

### Arrays
```pascal
var
    numeros: array[10] of integer;
    nomes: array[5] of string;
```

### Procedimentos
```pascal
procedure NomeProcedimento(parametro: tipo);
begin
    { comandos }
end;
```

### Funções
```pascal
function NomeFuncao(parametro: tipo): tipo_retorno;
begin
    { comandos }
    return valor;
end;
```

## Comandos

### Atribuição
```pascal
x := 10;
array[indice] := valor;
```

### Entrada e Saída
```pascal
readln(variavel);
writeln('texto', variavel);
```

### Controle de Fluxo

#### If-Then-Else
```pascal
if condicao then
    comando
else
    comando;
```

#### While
```pascal
while condicao do
    comando;
```

#### For
```pascal
for variavel := inicio to fim do
    comando;
```

## Expressões

### Operadores Aritméticos
- `+` (soma)
- `-` (subtração)
- `*` (multiplicação)
- `/` (divisão real)
- `div` (divisão inteira)
- `mod` (resto da divisão)

### Operadores Relacionais
- `=` (igual)
- `<>` (diferente)
- `<` (menor que)
- `>` (maior que)
- `<=` (menor ou igual)
- `>=` (maior ou igual)

### Operadores Lógicos
- `and` (e lógico)
- `or` (ou lógico)
- `not` (negação)

## Tipos de Dados

### Básicos
- `integer`: números inteiros
- `real`: números reais
- `boolean`: verdadeiro/falso
- `string`: texto

### Literais
- Inteiros: `123`, `-456`
- Reais: `3.14`, `-2.5`
- Booleanos: `true`, `false`
- Strings: `'texto'`, `"texto"`

## Comentários

### Chaves
```pascal
{ Este é um comentário }
```

### Barra dupla
```pascal
// Este é um comentário de linha
```
