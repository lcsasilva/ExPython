import random
n = random.randint(0, 5)

chute = int(input('Em qual número estou pensando, de 0 à 5: '))

if chute == n:
    print('Parabéns, você acertou! o número era {}!'.format(n))
else:
    print('Você errou! o número era {}'.format(n))