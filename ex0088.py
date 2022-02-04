import random
from time import sleep

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
jogo = list()
if jogos <= 0:
    print('Até logo.')
else:
    for c in range(0, jogos):
        jogo = list(range(1, 61))
        random.shuffle(jogo)
        print(f'Jogo {c+1}: {jogo[0:6]}')
        sleep(1)