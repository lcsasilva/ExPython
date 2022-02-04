import random

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

num = [n1, n2, n3]
num.sort()

print('O maior número é {} e o menor {}.'.format(num[-1], num[0]))
