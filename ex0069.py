maioridade = homens = mulheresmenos = 0
stop = 'N'
sexo = ''
print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*20)
while stop not in 'S':
    while True:
        idade = int(input('Qual é a idade? '))
        if idade > 0:
            while True:
                sexo = str(input('Qual é o sexo? [M/F]')).upper().strip()[0]
                if sexo in 'MF':
                    break
        break
    if idade > 18:
        maioridade += 1
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade <= 20:
        mulheresmenos += 1
    print('-='*20)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-='*20)
    if continuar == 'N':
        break
print('-'*30)
print(f'{maioridade} pessoas tem mais de 18 anos')
print('-'*30)
print(f'{homens} homens foram cadastrados.')
print('-'*30)
print(f'{mulheresmenos} mulheres tem menos de 20 anos.')
print('-'*30)