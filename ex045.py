print(100 * '-=')
print(20 * ' \033[30;0;42m JoKenPo\033[m \033[32;0;43m JoKenPo\033[m')
print(100 * '-=')
print(20 * ' \033[32;0;43m JoKenPo\033[m \033[30;0;42m JoKenPo\033[m')
print(100 * '-=')

import random
from time import sleep

jogador = int(input('[0] - PEDRA\n'
                    '[1] - PAPEL\n'
                    '[2] - TESOURA\n'
                    '\033[31;1mFaça sua escolha:  '))
maquina = random.randint(0, 2)

itens = ('Pedra', 'Papel', 'Tesoura')

if jogador > 2 or jogador < 0:
    print('Escolha uma opção válida!')
else:
    sleep(1)
    print('\033[34m Jo\033[m')
    sleep(1)
    print('\033[31m Ken\033[m')
    sleep(1)
    print('\033[36m Po\033[m')
    sleep(1)

    if maquina == 0 and jogador == 1 or maquina == 1 and jogador == 2 or maquina == 2 and jogador == 0:
        print('Computador \033[1;33m{}\033[m  \033[1;31mVS\033[m \033[1;33m{}\033[m Jogador'.format(itens[maquina], itens[jogador]))
        print('VOCÊ GANHOU!!!')

    elif jogador == 0 and maquina == 1 or jogador == 1 and maquina == 2 or jogador == 2 and maquina == 0:
        print('Computador \033[1;33m{}\033[m  \033[1;31mVS\033[m \033[1;33m{}\033[m Jogador'.format(itens[maquina], itens[jogador]))
        print('VOCE PERDEU!!!')

    elif maquina == jogador:
        print('Computador \033[1;33m{}\033[m  \033[1;31mVS\033[m \033[1;33m{}\033[m Jogador'.format(itens[maquina], itens[jogador]))
        print('EMPATE!!!')
