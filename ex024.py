cidade = input('Em qual cidade você mora?: ').strip()

print('Verificando se possuí "santo"... ')
cidade2 = cidade.lower()
print('santo' in cidade2)

print(cidade2[:5] == 'santo')