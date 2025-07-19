# Sintaxe Pascal Suportada

## Estrutura Básica de Programa

```pascal
program NomePrograma;
{ Seção de declarações de variáveis }
var
    variavel1: tipo1;
    variavel2: tipo2;
    
{ Seção de procedimentos - opcional }
procedure NomeProcedimento;
begin
    { comandos do procedimento }
end;

{ Programa principal }
begin
    { comandos principais }
end.
```

## Declarações

### Variáveis
```pascal
var
    contador, idade: integer;        { números inteiros }
    altura, peso: real;             { números reais }
    nome, sobrenome: string;        { strings/texto }
    ativo, concluido: boolean;      { valores lógicos }
```

**Tipos Suportados:**
- `integer` - números inteiros (ex: 42, -10, 0)
- `real` - números decimais (ex: 3.14, -2.5, 0.0)  
- `string` - texto entre aspas (ex: 'Olá mundo')
- `boolean` - valores lógicos (true ou false)

### Arrays (Vetores)
```pascal
var
    numeros: array[10] of integer;     { 10 inteiros: índices 0-9 }
    notas: array[5] of real;          { 5 reais: índices 0-4 }
    nomes: array[3] of string;        { 3 strings: índices 0-2 }
```

**Características:**
- Sempre unidimensionais (apenas vetores, não matrizes)
- Indexação baseada em zero (0, 1, 2, ...)
- Tamanho fixo definido na declaração

### Procedimentos
```pascal
procedure NomeProcedimento;
begin
    writeln('Procedimento sem parâmetros');
end;

procedure ComParametros(valor: integer; texto: string);
begin
    writeln('Valor: ', valor);
    writeln('Texto: ', texto);
end;
```

**Limitações:**
- Não há suporte a funções que retornam valores
- Apenas procedimentos (sem return)
- Parâmetros passados por valor

## Comandos e Operações

### Atribuição
```pascal
{ Variáveis simples }
x := 10;
nome := 'João';
ativo := true;
altura := 1.75;

{ Arrays }
numeros[0] := 42;
nomes[1] := 'Maria';
```

### Entrada e Saída
```pascal
{ Entrada de dados }
readln(idade);           { lê um inteiro }
readln(nome);            { lê uma string }

{ Saída de dados }
writeln('Olá mundo');    { imprime texto }
writeln(idade);          { imprime variável }
writeln('Idade: ', idade); { imprime texto e variável }
```

### Estruturas de Controle de Fluxo

#### Condicional If-Then-Else
```pascal
{ If simples }
if idade >= 18 then
    writeln('Maior de idade');

{ If-else }
if nota >= 7.0 then
    writeln('Aprovado')
else
    writeln('Reprovado');

{ If aninhado }
if idade >= 18 then begin
    writeln('Maior de idade');
    if idade >= 65 then
        writeln('Idoso');
end;
```

#### Loop While
```pascal
{ While simples }
while contador < 10 do begin
    writeln(contador);
    contador := contador + 1;
end;

{ While com condição complexa }
while (x > 0) and (y < 100) do begin
    x := x - 1;
    y := y + 2;
end;
```

#### Loop For
```pascal
{ For crescente }
for i := 1 to 10 do
    writeln('Número: ', i);

{ For com array }
for i := 0 to 4 do
    numeros[i] := i * 2;

{ For aninhado }
for i := 1 to 5 do begin
    for j := 1 to 3 do
        writeln(i, ' - ', j);
end;
```

## Operadores

### Operadores Aritméticos
```pascal
resultado := a + b;      { soma }
resultado := a - b;      { subtração }  
resultado := a * b;      { multiplicação }
resultado := a div b;    { divisão inteira }
resultado := a mod b;    { resto da divisão }
```

### Operadores Relacionais  
```pascal
if a = b then ...        { igual }
if a <> b then ...       { diferente }
if a < b then ...        { menor }
if a > b then ...        { maior }
if a <= b then ...       { menor ou igual }
if a >= b then ...       { maior ou igual }
```

### Operadores Lógicos
```pascal
if (a > 0) and (b > 0) then ...    { E lógico }
if (a = 0) or (b = 0) then ...     { OU lógico }
if not ativo then ...              { NÃO lógico }
```

## Comentários

### Comentários de Bloco
```pascal
{ Este é um comentário de bloco
  que pode ocupar múltiplas linhas }
program Exemplo;
```

### Comentários de Linha
```pascal
writeln('Hello'); // Este é um comentário de linha
x := 10;          // Comentário no final da linha
```

## Exemplos Práticos

### Programa Completo
```pascal
program ExemploCompleto;
var
    numeros: array[5] of integer;
    i, soma, media: integer;
begin
    { Entrada de dados }
    writeln('Digite 5 números:');
    for i := 0 to 4 do begin
        writeln('Número ', i + 1, ':');
        readln(numeros[i]);
    end;
    
    { Processamento }
    soma := 0;
    for i := 0 to 4 do
        soma := soma + numeros[i];
    
    media := soma div 5;
    
    { Saída }
    writeln('Soma: ', soma);
    writeln('Média: ', media);
    
    { Análise }
    if media >= 8 then
        writeln('Excelente!')
    else if media >= 6 then
        writeln('Bom')
    else
        writeln('Pode melhorar');
end.
```