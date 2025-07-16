program ControleFluxo;
var
    i, n: integer;
    eh_par: boolean;
begin
    writeln('=== Controle de Fluxo ===');
    
    { Exemplo de FOR }
    writeln('Contando de 1 a 10:');
    for i := 1 to 10 do
        writeln(i);
    
    { Exemplo de WHILE }
    writeln('Contando regressivo de 5 a 1:');
    i := 5;
    while i > 0 do
    begin
        writeln(i);
        i := i - 1;
    end;
    
    { Exemplo de IF-THEN-ELSE }
    writeln('Digite um número para verificar se é par:');
    readln(n);
    
    eh_par := (n mod 2) = 0;
    
    if eh_par then
        writeln(n, ' é par')
    else
        writeln(n, ' é ímpar');
end.
