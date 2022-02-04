lista = []

while True:
    lista.append(int(input('Digite um número? ')))
    continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if continuar in 'Nn':
        break


print(f'Os valores digitados ordenados de forma decrescente\n {sorted(lista, reverse=True)}')

print('-'*20)

print(f'No total foram digitados {len(lista)}')

print('-'*20)

if lista in 5:
    print(f'O valor 5 foi digitado e está na posição {lista.index(5)} lista.')
else:
    print('O valor 5 não foi digitado.')

