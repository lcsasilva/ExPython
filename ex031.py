dist = float(input('Quantos KMs de viagem?: '))
preco = dist * 0.50 if dist <= 200 else distancia * 0.45
print('O preço da sua passagem é R${:.2f}!'.format(preco))

'''if dist >= 200:
    valor = dist*0.45
    print('O valor da sua passagem é R${:.2f}'.format(valor))
else:
    valor = dist*0.50
    print('O valor da sua passagem é R${:.2f}'.format(valor))'''




    