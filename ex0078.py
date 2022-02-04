lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posiçãp {c}: ')))
print(f'O maior valor digita foi {max(lista)} e está na posição {lista.index(max(lista))+1}')
print(f'O menor valor digita fio {min(lista)} e está na posição {lista.index(min(lista))+1}')
