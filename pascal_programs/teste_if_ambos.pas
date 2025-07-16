program TesteIfSemBegin;
var
    x: integer;
begin
    x := 10;
    
    { Teste 1: if-then-else sem begin }
    if x > 5 then
        writeln('x é maior que 5')
    else
        writeln('x é menor ou igual a 5');
    
    { Teste 2: if-then-else com begin }
    if x > 15 then
    begin
        writeln('x é maior que 15');
    end
    else
    begin
        writeln('x é menor ou igual a 15');
    end;
    
    { Teste 3: if-then-else misto }
    if x = 10 then
        writeln('x é igual a 10')
    else
    begin
        writeln('x não é igual a 10');
        writeln('Valor de x: ', x);
    end;
    
    writeln('Fim do programa');
end.
