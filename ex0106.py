def titulo(a):
    tm = len(a) + 2
    print('~' * tm)
    print(f'{a:^{tm}}')
    print('~' * tm)


def ajuda(comando):
    help(comando)


from time import sleep
#programa principal

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    sleep(1)
    comando = str(input('Função da biblioteca > '))
    if comando.lower() in 'fim':
        break
    sleep(1)
    titulo(f'Acessando o manual do comando "{comando}"')
    sleep(1)
    ajuda(comando)
