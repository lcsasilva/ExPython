palavra = str(input('Digite o texto: '))

def escreva(a):
    tm = len(a) + 4
    print('~' * tm)
    print(f'{a:^{tm}}')
    print('~' * tm)

escreva(palavra)