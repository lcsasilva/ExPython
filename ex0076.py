'''listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10)

for c in range(0, len(listagem), 2):
    print(f'{listagem[c]}..........R${listagem[c+1]}')'''


listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10)
print('-'*40)
print('LISTAGEM DE PREÇOS')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:*<30}',end=' ')
    else:
        print(f'R${listagem[pos]:<5.2f}')
print('-'*40)