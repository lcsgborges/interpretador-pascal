program OrdenacaoSimples;
{
  Algoritmo elaborado: Ordenação por seleção (Selection Sort)
  Demonstra algoritmo O(n²) com busca do menor elemento
}
var
    numeros: array[5] of integer;
    n, i, j, menor_idx, temp: integer;

begin
    writeln('=== Algoritmo de Ordenação por Seleção ===');
    writeln('Este programa demonstra um algoritmo elaborado de ordenação');
    writeln('');
    
    n := 5;
    writeln('Digite ', n, ' números para ordenar:');
    
    { Ler números }
    for i := 0 to n - 1 do
    begin
        writeln('Número ', i + 1, ':');
        readln(numeros[i]);
    end;
    
    { Exibir array original }
    writeln('');
    writeln('Array original:');
    for i := 0 to n - 1 do
        writeln('  [', i, '] = ', numeros[i]);
    
    { Algoritmo Selection Sort }
    writeln('');
    writeln('=== Executando Selection Sort ===');
    
    for i := 0 to n - 2 do
    begin
        { Encontrar o menor elemento }
        menor_idx := i;
        for j := i + 1 to n - 1 do
        begin
            if numeros[j] < numeros[menor_idx] then
                menor_idx := j;
        end;
        
        { Trocar elementos se necessário }
        if menor_idx <> i then
        begin
            writeln('Trocando posições ', i, ' e ', menor_idx, ' (', numeros[i], ' <-> ', numeros[menor_idx], ')');
            temp := numeros[i];
            numeros[i] := numeros[menor_idx];
            numeros[menor_idx] := temp;
        end;
    end;
    
    { Exibir array ordenado }
    writeln('');
    writeln('Array ordenado:');
    for i := 0 to n - 1 do
        writeln('  [', i, '] = ', numeros[i]);
    
    { Demonstrar busca linear }
    writeln('');
    writeln('=== Busca Linear ===');
    writeln('Digite um número para buscar:');
    readln(temp);
    
    j := -1;  { Posição não encontrada }
    for i := 0 to n - 1 do
    begin
        if numeros[i] = temp then
        begin
            j := i;
            i := n;  { Para sair do loop }
        end;
    end;
    
    if j = -1 then
        writeln('Número ', temp, ' não encontrado no array')
    else
        writeln('Número ', temp, ' encontrado na posição ', j);
    
    writeln('');
    writeln('Algoritmo concluído! Complexidade: O(n²)');
end.
