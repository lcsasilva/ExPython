lista = []
par = []
impar = []

while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if continuar in 'n':
        break
    else:
        lista.append(int(input('Digite um número: ')))
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f'A lista completa é {lista}')

print(f'A lista de pares é {par}')

print(f'A lista de ímpar é {impar}')

