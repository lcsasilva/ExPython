from time import sleep
n1 = 0
n2 = 0
fim = 0
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
while fim != 5:
    sleep(1)
    fim = int(input('Você deseja: \n [1] somar\n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa \n opção: '))
    if fim == 1:
        print('A soma do número {} com o número {} resulta em {}'.format(n1, n2, n1+n2))
    elif fim == 2:
        print('O número {} mulplicado pelo {} resulta em {}.'.format(n1, n2, n1*n2))
    elif fim == 3:
        if n1 > n2:
            print('O número {} é maior que {}.'.format(n1, n2))
        elif n1 == n2 or n2 == n1:
            print('Os números {} e {} são iguais.'.format(n1, n2))
        else:
            print('O número {} é maior que {}.'.format(n2, n1))
    elif fim == 4:
        n1 = int(input('Digite um número inteiro: '))
        n2 = int(input('Digite outro número inteiro: '))
print('FIM')