lista = list()
dados = dict()
media = 0
mulheres = list()
idade_acima = list()
while True:
    nome = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'MF':
            break
        else:
            print('Digite um sexo válido.')
    idade = int(input('Idade: '))
    media += idade
    dados['nome'] = nome
    dados['sexo'] = sexo
    dados['idade'] = idade
    lista.append(dados.copy())
    if sexo in 'F': # mulheres cadastradas C
        mulheres.append(dados.copy())
    dados.clear()
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-='*30)
print(f'O grupo term {len(lista)} pessoas.') # quantidade de pessoas A
print('-='*30)
print(f'A média de idade é de {media/len(lista)} anos.')
print('=-'*30)
if mulheres != 0:     # mulheres cadastradas C
    print(f'As mulheres cadastradas foram:', end=' ')
    for p in range(0, len(mulheres)):
        print(f'{mulheres[p]["nome"]}', end=' ')
print()
print('-='*30)
print(f'Lista das pessoas que estão acima da média: ')


for c in range(0, len(lista)):
    if lista[c]["idade"] > media/len(lista):
        print(f'Nome = {lista[c]["nome"]}; sexo = {lista[c]["sexo"]}; idade = {lista[c]["idade"]}: ')
