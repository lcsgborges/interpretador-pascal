program ExemploCompleto;
var
    numeros: array[5] of integer;
    i, n, soma, maior: integer;

begin
    writeln('=== Demonstração do Interpretador Pascal ===');
    writeln('Este programa demonstra arrays e procedimentos');
    writeln('');
    
    n := 3;
    writeln('Vamos processar ', n, ' números:');
    
    { Preencher array }
    for i := 0 to n - 1 do
    begin
        writeln('Digite o número ', i + 1, ':');
        readln(numeros[i]);
    end;
    
    { Exibir array original }
    writeln('');
    writeln('Array original:');
    for i := 0 to n - 1 do
        writeln('  [', i, '] = ', numeros[i]);
    
    { Calcular estatísticas }
    soma := 0;
    maior := numeros[0];
    for i := 0 to n - 1 do
    begin
        soma := soma + numeros[i];
        if numeros[i] > maior then
            maior := numeros[i];
    end;
    
    writeln('');
    writeln('=== Estatísticas ===');
    writeln('Soma total: ', soma);
    writeln('Maior valor: ', maior);
    writeln('Média: ', soma div n);
    
    { Ordenar array (Bubble Sort simplificado) }
    writeln('');
    writeln('=== Ordenação ===');
    for i := 0 to n - 2 do
    begin
        if numeros[i] > numeros[i + 1] then
        begin
            { Trocar elementos }
            soma := numeros[i];      { Usar soma como variável temp }
            numeros[i] := numeros[i + 1];
            numeros[i + 1] := soma;
        end;
    end;
    
    writeln('Array após primeira passagem de ordenação:');
    for i := 0 to n - 1 do
        writeln('  [', i, '] = ', numeros[i]);
        
    writeln('');
    writeln('Demonstração concluída com sucesso!');
end.
