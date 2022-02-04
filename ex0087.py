lista = list()
dados = list()
par = []
maior = 0
for c in range(0, 3):
    dados.append((int(input(f'Digite um valor para [0, {c}]: '))))
    if c == 2:
        lista.append(dados[:])
        dados.clear()
for c in range(0, 3):
    dados.append((int(input(f'Digite um valor para [1, {c}]: '))))

    if c == 2:
        lista.append(dados[:])
        dados.clear()
for c in range(0, 3):
    dados.append((int(input(f'Digite um valor para [2, {c}]: '))))
    if c == 2:
        lista.append(dados[:])
        dados.clear()

for i, v in enumerate(lista):
    print(f'[{v[0]:^5}][{v[1]:^5}][{v[2]:^5}]')


print(f'A soma dos valores pares é {par}')

print(f'A soma dos valores da terceira coluna é {lista[0][2] + lista[1][2] + lista[2][2]}')


print(f'O maior valor da segunda linha é {max(lista[1])}')
