program ProcedimentosSimples;
{
  Demonstra uso básico de procedimentos em Pascal
}
var
    nome: string;
    idade: integer;

procedure Saudacao(n: string);
begin
    writeln('Olá, ', n, '! Bem-vindo ao programa Pascal!');
end;

procedure VerificarIdade(anos: integer);
begin
    if anos >= 18 then
        writeln('Você é maior de idade.')
    else
        writeln('Você é menor de idade.');
end;

procedure ExibirMenu();
begin
    writeln('=== Menu Principal ===');
    writeln('1. Informações pessoais');
    writeln('2. Verificar maioridade');
    writeln('3. Sair');
end;

begin
    writeln('=== Sistema de Cadastro ===');
    
    writeln('Digite seu nome:');
    readln(nome);
    
    writeln('Digite sua idade:');
    readln(idade);
    
    Saudacao(nome);
    VerificarIdade(idade);
    
    writeln('');
    ExibirMenu();
    writeln('Obrigado por usar o sistema!');
end.
