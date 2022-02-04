pesos = []

for pessoas in range(0, 5):
    peso = int(input('Digite o peso: '))
    pesos.append(peso)

pesos.sort()
print('A pessoa com maior peso é {}Kg e com menor peso é {}Kg.'.format(
    pesos[0], pesos[-1]
))