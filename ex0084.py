'''pessoas = list()
dados = list()
totp = 0
maiorpeso = list()
menorpeso = list()
while True:
    totp += 1
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    continuar = str(input('\nQuer continuar? [S/N] ')).strip().lower()
    pessoas.append(dados[:])
    if totp == 1:
        maiorpeso.append(dados[:])
        menorpeso.append(dados[:])
    if dados[1] > maiorpeso[0][1]:
        maiorpeso.clear()
        maiorpeso.append(dados[:])
    if dados[1] < menorpeso[0][1]:
        menorpeso.clear()
        menorpeso.append(dados[:])
    if dados[1] == maiorpeso[0][1]:
        maiorpeso.append(dados[:])
    if dados[1] == maiorpeso:
        maiorpeso.append(dados[:])
    dados.clear()
    if continuar in 'n':
        break
print('=-'*20)
print(f'Ao todo, você cadastrou {totp} pessoas.')
print(f'O maior peso foi de {maiorpeso[0][1]}Kg. Peso de ', end=' ')
for c in range(0, len(maiorpeso)):
    print(f'{maiorpeso[c][0]}', end=' ')
print(f'\nO menorpeso foi de {menorpeso[0][1]}Kg. Peso de ', end=' ')
for c in range(0, len(menorpeso)):
    print(f'{menorpeso[c][0]}', end=' ')'''

temp = list()
princ = list()
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    resposta = str(input('Quer continuar? [S/N]')).strip()[0]
    temp.clear()
    if resposta in 'Nn':
        break
print('-='*30)
print(f'Os dados foram {princ}')
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}')
print()
print(f'O menor peso foi de {men}Kg', end=' ')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}')