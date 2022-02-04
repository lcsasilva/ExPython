dias = int(input('O carro foi usado por quantos dias?: '))
preco = float(input('Quantos KMs rodados?: '))

diaria = 60
km = 0.15
total = (dias*diaria)+(preco*km)

print('O total a pagar é de R${:.2f}'.format(total))