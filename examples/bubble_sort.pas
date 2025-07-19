program OrdenacaoBubbleSort;
{
  Implementa o algoritmo de ordenação Bubble Sort para ordenar um array de inteiros
}
var
    numeros: array[5] of integer;
    n, i, j, temp: integer;
    trocou: boolean;

begin
    writeln('=== Programa de Ordenação Bubble Sort ===');
    n := 5;  { Tamanho fixo para simplicidade }
    
    writeln('Digite 5 números:');
    for i := 0 to n - 1 do
    begin
        writeln('Número ', i + 1, ': ');
        readln(numeros[i]);
    end;
    
    { Exibir array original }
    writeln('Array original:');
    for i := 0 to n - 1 do
    begin
        writeln('  [', i, '] = ', numeros[i]);
    end;
    
    { Bubble Sort }
    writeln('Ordenando...');
    for i := 0 to n - 2 do
    begin
        trocou := false;
        for j := 0 to n - 2 - i do
        begin
            if numeros[j] > numeros[j + 1] then
            begin
                { Troca os elementos }
                temp := numeros[j];
                numeros[j] := numeros[j + 1];
                numeros[j + 1] := temp;
                trocou := true;
                writeln('Trocando ', numeros[j + 1], ' <-> ', numeros[j]);
            end;
        end;
        
        { Se não houve troca, o array já está ordenado }
        if not trocou then
            i := n;  { Equivale ao break }
    end;
    
    { Exibir array ordenado }
    writeln('Array ordenado:');
    for i := 0 to n - 1 do
    begin
        writeln('  [', i, '] = ', numeros[i]);
    end;
    
    { Busca simples }
    writeln('Digite um número para buscar:');
    readln(temp);
    
    i := 0;
    while i < n do
    begin
        if numeros[i] = temp then
        begin
            writeln('Número ', temp, ' encontrado na posição ', i + 1);
            i := n + 1;  { Para sair do loop }
        end
        else
        begin
            i := i + 1;
        end;
    end;
    
    if i = n then  { Não encontrou }
        writeln('Número ', temp, ' não encontrado');
end.
