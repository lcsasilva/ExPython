n1 = float(input('Qual é a primeira nota?: '))
n2 = float(input('Qual é a segunda nota?: '))
m = (n1+n2)/2

if m < 5.0:
    print('REPROVADO')
elif m > 5.0 and m < 6.9:
    print('RECUPERAÇÂO')
elif m >= 7.0:
    print('APROVADO')