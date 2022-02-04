lista = list()
dados = list()
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