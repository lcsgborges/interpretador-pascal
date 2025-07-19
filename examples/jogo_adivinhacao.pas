program JogoAdvinhacao;
{
  Jogo de adivinhação que demonstra uso de:
  - Geração de números pseudo-aleatórios
  - Estruturas de controle
  - Contadores e validações
  - Procedimentos com parâmetros
}

var
    numeroSecreto, tentativa, numTentativas, maxTentativas: integer;
    acertou, jogando, valido: boolean;
    resposta: string;
    valor: integer;

{ Procedimento para definir número secreto fixo para demonstração }
procedure definirNumeroSecreto();
begin
    { Número secreto fixo para demonstração - em um jogo real seria aleatório }
    numeroSecreto := 42;
end;

{ Procedimento para exibir dicas }
procedure darDica(tentativa, numeroSecreto: integer);
begin
    if tentativa < numeroSecreto then
    begin
        writeln('Muito baixo! Tente um número maior.');
    end
    else if tentativa > numeroSecreto then
    begin
        writeln('Muito alto! Tente um número menor.');
    end;
end;

{ Procedimento para exibir resultado final }
procedure exibirResultado(acertou: boolean; numTentativas: integer; numeroSecreto: integer);
begin
    writeln('');
    writeln('=== RESULTADO ===');
    
    if acertou then
    begin
        writeln('Parabéns! Você acertou!');
        writeln('Número de tentativas: ', numTentativas);
        
        if numTentativas <= 3 then
            writeln('Excelente! Você é um mestre!')
        else if numTentativas <= 6 then
            writeln('Muito bom!')
        else
            writeln('Você conseguiu, mas pode melhorar!');
    end
    else
    begin
        writeln('Que pena! Você não conseguiu adivinhar.');
        writeln('O número secreto era: ', numeroSecreto);
        writeln('Tente novamente na próxima vez!');
    end;
end;

{ Procedimento para ler tentativa do usuário }
procedure lerTentativa(min, max: integer);
begin
    valido := false;
    
    while not valido do
    begin
        writeln('Digite um número entre ', min, ' e ', max, ':');
        readln(valor);
        
        if (valor >= min) and (valor <= max) then
        begin
            valido := true;
            tentativa := valor;
        end
        else
        begin
            writeln('Número inválido! Deve estar entre ', min, ' e ', max, '.');
        end;
    end;
end;

{ Procedimento principal do jogo }
procedure jogar();
begin
    { Configuração do jogo }
    writeln('=== JOGO DE ADIVINHAÇÃO ===');
    writeln('Vou pensar em um número entre 1 e 100.');
    writeln('Você tem até 10 tentativas para acertar!');
    writeln('');
    
    { Gerar número secreto }
    definirNumeroSecreto();
    maxTentativas := 10;
    numTentativas := 0;
    acertou := false;
    
    { Loop principal do jogo }
    while (numTentativas < maxTentativas) and (not acertou) do
    begin
        numTentativas := numTentativas + 1;
        writeln('Tentativa ', numTentativas, ' de ', maxTentativas);
        
        lerTentativa(1, 100);
        
        if tentativa = numeroSecreto then
        begin
            acertou := true;
        end
        else
        begin
            darDica(tentativa, numeroSecreto);
            writeln('Tentativas restantes: ', maxTentativas - numTentativas);
            writeln('');
        end;
    end;
    
    { Exibir resultado }
    exibirResultado(acertou, numTentativas, numeroSecreto);
end;

{ Procedimento para perguntar se quer jogar novamente }
procedure jogarNovamente();
begin
    writeln('');
    writeln('Deseja jogar novamente? (s/n):');
    readln(resposta);
    
    jogando := (resposta = 's') or (resposta = 'S') or (resposta = 'sim') or (resposta = 'SIM');
end;

{ Programa principal }
begin
    writeln('Bem-vindo ao Jogo de Adivinhação!');
    
    jogando := true;
    while jogando do
    begin
        jogar();
        jogarNovamente();
    end;
    
    writeln('');
    writeln('Obrigado por jogar! Até a próxima!');
end.
