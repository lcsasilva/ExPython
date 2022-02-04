n = int(input('Digite um número para saber a taboada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(c, n, c*n))