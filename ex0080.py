lista = []

for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Primeiro valor da lista adicionado!')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1


print(lista)