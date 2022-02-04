vl = int(input('Qual velocidade do carro?: '))

if vl > 80:
    print('O limite da via é 80Km/h, você foi multado!')
    km = vl - 80
    multa = km*7
    print('E o valor a ser pago é R${:.2f}'.format(multa))
else:
    print('Continue dirigindo com segurança.')

