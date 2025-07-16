program Calculadora;
var
    a, b: integer;
    resultado: integer;
begin
    writeln('=== Calculadora Simples ===');
    writeln('Digite dois números:');
    
    readln(a, b);
    
    resultado := a + b;
    writeln('Soma: ', resultado);
    
    resultado := a - b;
    writeln('Subtração: ', resultado);
    
    resultado := a * b;
    writeln('Multiplicação: ', resultado);
    
    if b <> 0 then
    begin
        resultado := a div b;
        writeln('Divisão inteira: ', resultado);
        
        resultado := a mod b;
        writeln('Resto da divisão: ', resultado);
    end
    else
        writeln('Não é possível dividir por zero!');
end.
