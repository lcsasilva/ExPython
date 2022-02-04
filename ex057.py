'''sexo = ''

while sexo != 'mf':
    sexo = str(input('Qual é o seu sexo? [M/F]: ')).lower().strip()[0]

if sexo == 'm':
    print('O sexo escolhido foi Masculino.')
else:
    print('o Sexo escolhido foi feminino.')
'''


sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
if sexo == 'Mm':
    print('Sexo masculino registrado com sucesso.')
else:
    print('Sexo feminino registrado com sucesso.')
