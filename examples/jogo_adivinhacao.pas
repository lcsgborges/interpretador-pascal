program JogoAdvinhacao;
{
  Jogo de adivinhação que demonstra uso de:
  - Geração de números aleatórios (simulada)
  - Estruturas de controle
  - Contadores e validações
}

var
    numeroSecreto, tentativa, numTentativas, maxTentativas: integer;
    acertou, jogando: boolean;

{ Função para simular geração de número aleatório }
function gerarNumeroAleatorio(min, max: integer): integer;
var
    seed: integer;
begin
    { Simulação simples de número aleatório baseado em entrada do usuário }
    writeln('Para gerar número aleatório, digite um número qualquer:');
    readln(seed);
    
    { Fórmula simples para gerar número pseudo-aleatório }
    seed := (seed * 1103515245 + 12345) mod 2147483647;
    gerarNumeroAleatorio := (seed mod (max - min + 1)) + min;
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
        writeln('🎉 Parabéns! Você acertou!');
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
        writeln('😞 Que pena! Você não conseguiu adivinhar.');
        writeln('O número secreto era: ', numeroSecreto);
        writeln('Tente novamente na próxima vez!');
    end;
end;

{ Função para validar entrada do usuário }
function lerTentativa(min, max: integer): integer;
var
    valor: integer;
    valido: boolean;
begin
    valido := false;
    
    repeat
        writeln('Digite um número entre ', min, ' e ', max, ':');
        readln(valor);
        
        if (valor >= min) and (valor <= max) then
        begin
            valido := true;
            lerTentativa := valor;
        end
        else
        begin
            writeln('Número inválido! Deve estar entre ', min, ' e ', max, '.');
        end;
    until valido;
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
    numeroSecreto := gerarNumeroAleatorio(1, 100);
    maxTentativas := 10;
    numTentativas := 0;
    acertou := false;
    
    { Loop principal do jogo }
    while (numTentativas < maxTentativas) and (not acertou) do
    begin
        numTentativas := numTentativas + 1;
        writeln('Tentativa ', numTentativas, ' de ', maxTentativas);
        
        tentativa := lerTentativa(1, 100);
        
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

{ Função para perguntar se quer jogar novamente }
function jogarNovamente(): boolean;
var
    resposta: string;
begin
    writeln('');
    writeln('Deseja jogar novamente? (s/n):');
    readln(resposta);
    
    jogarNovamente := (resposta = 's') or (resposta = 'S') or (resposta = 'sim') or (resposta = 'SIM');
end;

{ Programa principal }
begin
    writeln('🎮 Bem-vindo ao Jogo de Adivinhação! 🎮');
    
    repeat
        jogar();
        jogando := jogarNovamente();
    until not jogando;
    
    writeln('');
    writeln('Obrigado por jogar! Até a próxima! 👋');
end.
