'''from random import randint

random = []
lista = random
maior = menor = 0
for c in range(0, 5):
    n = randint(0, 10)
    random.append(n)

    if c == 1:
        menor = n
        maior = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
print(f'Os valores sorteados foram: {lista}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')'''

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end=' ')

for n in numeros:
    print(f'{n}', end=' ')
print(f'\n O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
