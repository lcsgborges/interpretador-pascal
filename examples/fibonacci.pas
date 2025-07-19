program Fibonacci;
var
    n, i, a, b, temp: integer;

begin
    writeln('=== Sequência de Fibonacci ===');
    writeln('Digite quantos números da sequência deseja ver:');
    readln(n);
    
    if n <= 0 then
    begin
        writeln('Número deve ser positivo!');
    end
    else
    begin
        writeln('Sequência de Fibonacci:');
        
        a := 0;
        b := 1;
        
        if n >= 1 then
            writeln('Fibonacci[1] = ', a);
        
        if n >= 2 then
            writeln('Fibonacci[2] = ', b);
        
        for i := 3 to n do
        begin
            temp := a + b;
            writeln('Fibonacci[', i, '] = ', temp);
            a := b;
            b := temp;
        end;
    end;
end.
