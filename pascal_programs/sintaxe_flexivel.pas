program ExemploSintaxeFlexivel;
var
    x, y: integer;
    nome: string;
begin
    writeln('=== Demonstração de Sintaxe Flexível ===');
    
    x := 10;
    y := 5;
    
    { Exemplo 1: if-then-else sem begin-end }
    writeln('Exemplo 1: if-then-else sem begin-end');
    if x > y then
        writeln('x é maior que y')
    else
        writeln('x é menor ou igual a y');
    
    { Exemplo 2: if-then-else com begin-end }
    writeln('Exemplo 2: if-then-else com begin-end');
    if x = 10 then
    begin
        writeln('x é igual a 10');
        writeln('Valor confirmado!');
    end
    else
    begin
        writeln('x não é igual a 10');
        writeln('Valor: ', x);
    end;
    
    { Exemplo 3: if-then-else misto }
    writeln('Exemplo 3: if-then-else misto');
    if y < 3 then
        writeln('y é menor que 3')
    else
    begin
        writeln('y é maior ou igual a 3');
        writeln('Valor de y: ', y);
        writeln('Calculando y * 2 = ', y * 2);
    end;
    
    { Exemplo 4: if-then sem else }
    writeln('Exemplo 4: if-then sem else');
    if x > 0 then
        writeln('x é positivo');
    
    writeln('Fim da demonstração');
end.
