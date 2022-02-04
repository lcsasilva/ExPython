lista = []

while True:
    numero = int(input('Digite um valor: '))
    if numero in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
    lista.append(numero)
    continuar = str(input('Deseja continuar? [S/N] ')).lower().split()[0]
    if continuar in 'n':
        break
lista.sort()
print(f'Você digitou os valores {lista}')
