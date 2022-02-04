'''import datetime


def voto(ano):
    a = datetime.date.today().year - ano
    if a >= 65:
        print(f'Com {a} anos: VOTO OPCIONAL.')
    elif a >= 48:
        print(f'Com {a} anos: VOTO OBRIGATÓRIO.')
    elif a >= 18:
        print(f'Com {a} anos: VOTO OBRIGATÓRIO.')
    else:
        print(f'Com {a} anos: NÂO VOTA.')




#programa principal

verifica = int(input('Em que ano você nasceu? '))
voto(verifica)'''


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

print(voto(2000))