print('PROGRAMA TABUADA')
print('-'*30)
while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero <= 0:
        break
    else:
        for c in range(1, 11):
            print(f'{numero} x {c} = {numero*c}')

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')