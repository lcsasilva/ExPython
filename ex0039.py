import datetime

nascimento = int(input('Qual seu ano de nascimento?: '))
ano = datetime.date.today().year
verifica = len(str(nascimento))
idade = ano - nascimento

if verifica == 4:
    print('Você nasceu em {}, então você tem {} anos.'.format(nascimento, idade))
    if idade == 18:
        print('Você está na idade de alistamento!')
    elif idade < 18:
        alis = 18 - idade
        if alis < 1:
            print('Você ainda é novo para o alistamento, ainda faltam {} anos.'.format(alis))
        else:
            print('Você ainda é novo para o alistamento, ainda falta {} ano.'.format(alis))
    elif idade > 18:
        alis = idade - 18
        if alis < 1:
            print('Você já deveria ter se alistado. Está {} anos atrasado'.format(alis))
        else:
            print('Você já deveria ter se a alistado. Está {} ano atrasado.'.format(alis))

else:
    print('A data precisa conter 4 digitos.')