import random
from time import sleep
from operator import itemgetter
jogadores = dict()
jogadores['jogador1'] = random.randint(1, 6)
jogadores['jogador2'] = random.randint(1, 6)
jogadores['jogador3'] = random.randint(1, 6)
jogadores['jogador4'] = random.randint(1, 6)
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
cont = 0

print('Ranking dos jogadores;')
'''for i in sorted(jogadores, key = jogadores.get, reverse=True):
    cont += 1
    print(f'{cont}° lugar: {i} com {jogadores[i]}')
    sleep(0.5)'''
ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
print(ranking)
