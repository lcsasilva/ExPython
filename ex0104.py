def leiaint(a):
    while True:
        numero = str(input(f'{a}'))
        if numero.isnumeric():
            break
        else:
            print('ERRO! Digite um número inteiro válido.')
    return numero

#programa principal
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}.')