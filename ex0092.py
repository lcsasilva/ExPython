import datetime
import time
ano = datetime.date.today().year
cadastro = dict()

while True:
    cadastro['nome'] = str(input('Nome: '))
    nascimento = int(input('Ano de nascimento: '))
    cadastro['idade'] = ano - nascimento
    ctps = int(input('Carteira de trabalho (0 não tem): '))
    if ctps != 0:
        cadastro['CTPS'] = ctps
        contratacao = int(input('Ano de contratação: '))
        cadastro['contratação'] = contratacao
        cadastro['Aposentadoria'] = (ano - contratacao) + 35
        cadastro['salário'] = str(input('Salário: '))
    break
print('-='*30)

for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')