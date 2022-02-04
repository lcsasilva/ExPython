s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    t = n % 2
    if t == 0:
        s = s + n
        cont += 1
print('Você digitou {} números pares e a soma é {}.'.format(
    cont, s
))