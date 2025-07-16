program ProcedureFuncao;
var
    x, y, resultado: integer;

procedure cumprimentar;
begin
    writeln('Olá! Bem-vindo ao programa!');
end;

function somar(a, b: integer): integer;
begin
    return a + b;
end;

function fatorial(n: integer): integer;
begin
    if n <= 1 then
        return 1
    else
        return n * fatorial(n - 1);
end;

procedure mostrar_resultado(valor: integer);
begin
    writeln('O resultado é: ', valor);
end;

begin
    writeln('=== Procedimentos e Funções ===');
    
    cumprimentar;
    
    writeln('Digite dois números:');
    readln(x, y);
    
    resultado := somar(x, y);
    mostrar_resultado(resultado);
    
    writeln('Calculando fatorial de ', x, ':');
    resultado := fatorial(x);
    mostrar_resultado(resultado);
end.
