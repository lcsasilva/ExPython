import random
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advininhar qual foi?')

'''maquina = random.randint(0, 10)
jogador = 0
cont = 0
while jogador != maquina:
    jogador = int(input('Estou pensando em um número de 0 à 10. Qual é seu palpite?'))
    if jogador > 0-1:
        cont += 1
print('Você acertou depois de {} tentativas.\n estava pensando no número {}, '.format(cont, jogador))
'''

computador = random.randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print('Acertou com {} tentativas, parabéns!'.format(palpites))