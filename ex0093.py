cadastro = dict()

cadastro['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou?: '))
cadastro['partidas'] = partidas
gol = []
for c in range(0, partidas):
    gol.append(int(input(f'Quantos gols na partida {c+1}?: ')))
cadastro['gols'] = gol
cadastro['total'] = sum(gol)
print('-='*30)
print(cadastro)
print('-='*30)
for k, v in cadastro.items():
    print(f'O campo {k} tem o valor {v}.')

print(f'O jogador {cadastro["nome"]} jogou {cadastro["partidas"]} partidas.')
print('-='*30)
cont = 0
for g in cadastro['gols']:
    cont += 1
    print(f'   => Na partida {cont} fez {g} gols.')
print(f'Foi um total de {sum(gol)} gols.')

