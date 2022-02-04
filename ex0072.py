tupla = ('zero', 'um' ,'dois', 'três','quatro' , 'cinco', 'seis','sete', 'oitro', 'nove', 'dez')

while True:
    numero = int(input('Digite um número entre 0 e 10: '))

    if numero > 10 and numero < 0:
        print('Tente novamente.', end=' ')
    elif numero <= 10 and numero >= 0:
        print(f'Você digitou o número {tupla[numero]}')