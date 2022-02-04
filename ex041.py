import datetime
nascimento = int(input('DIGITE SEU ANO DE NASCIMENTO: '))
ano = datetime.date.today().year
idade = ano - nascimento

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')