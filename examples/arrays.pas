program Arrays;
var
    numeros: array[5] of integer;
    i, soma: integer;
begin
    writeln('=== Exemplo com Arrays ===');
    
    { Preenchendo o array }
    writeln('Digite 5 números:');
    for i := 0 to 4 do
    begin
        writeln('Número ', i + 1, ':');
        readln(numeros[i]);
    end;
    
    { Calculando a soma }
    soma := 0;
    for i := 0 to 4 do
        soma := soma + numeros[i];
    
    { Mostrando resultados }
    writeln('Números digitados:');
    for i := 0 to 4 do
        writeln('numeros[', i, '] = ', numeros[i]);
    
    writeln('Soma total: ', soma);
end.
