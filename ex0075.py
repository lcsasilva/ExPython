'''a = pares = 0
pos = 0
lista = []
tupla = (lista)

for c in range(0, 4):
    n = int(input(f'Digite o {c+1}° número: '))
    lista.append(n)
    if n == 9:
        a += 1
    elif n % 2 == 0:
        pares += 1

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {a} vezes')
print(f'O valor 3 apareceu na {tupla.index(3)+1}° posição')
print(f'Os valores pares digitados foram {pares}')'''

numero = (int(input('Digite um número: ')),
            int(input('Digite um número: ')),
            int(input('Digite um número: ')),
            int(input('Digite um número: ')))
print(f'Você digitou os valores {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)}° posição')
else:
    print('O valor 3 não foi digitado em nehuma posição.')
print(f'Os valores pares digitados foram ', end=' ')

for n in numero:
    if n % 2 == 0:
        print(n, end=' ')


