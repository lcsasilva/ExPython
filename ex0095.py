'''jogadores = list()
dados = dict()
contador = 0
#Cadastrando os jogadores
while True:
    dados['nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    dados['partidas'] = partidas
    gol = []
    for c in range(0, partidas):
        gol.append(int(input(f'Quantos gols na partida {c+1}? ')))
    dados['gols'] = gol
    dados['total'] = sum(gol)
    jogadores.append(dados.copy())
    dados.clear()
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        print('-='*50)
        break
    else:
        print('-' * 50)

#printando tabela com jogadores
print('cod  nome         gols                 total')
print('-'*50)
for i, v in enumerate(jogadores):
    print(f'{i:<}     {v["nome"]}          {v["gols"]}                 {v["total"]}')
print('-'*30)

#vendo dados pelo index do jogador na lista
while True:
    qual = str(input('Mostrar dados de qual jogador? [999 encerrar] '))
    if qual == 999:
        print('Finalizando...')
        break
    if qual > len(jogadores):
        print('Digite um index válido.')
    else:
        for c in range(0, jogadores[qual]['partidas']):
            print(f'No jogo {c+1} fez {jogadores[qual]["gols"][c]} gols')'''
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'      Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas com S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'`{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'      No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')