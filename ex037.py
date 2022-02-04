import math

num = int(input('Digite um número inteiro: '))

con = int(input('Para qual base deseja converter:\n'
                '1 - binário\n'
                '2 - octal\n'
                '3 - hexadeciaml\n'
                'Digite o número correspondente: '))

if con == 1:
    print('Seu número {} em binário fica {}.'.format(num, bin(num)[2:]))
elif con == 2:
    print('Seu número {} em octal fica {}.'.format(num, oct(num)[2:]))
elif con == 3:
    print('Seu número {} em hexadecimal fica {}.'.format(num, hex(num)[2:]))
else:
    print('Você precisa digitar umas das opções.')