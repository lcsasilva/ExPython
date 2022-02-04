lista = list()
par = list()
impar = list()

for c in range(0, 7):
    numero = int(input(f'Digite o {c+1}° valor: '))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
par.sort()
impar.sort()
lista.append(par[:])
lista.append(impar[:])
print('=-'*30)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores impares digitados foram: {impar}')