n1 = int(input('Digita um número: '))
r1 = int(input('Digite a razão da pa: '))
decimo = n1 + (10 - 1) * r1
for c in range(n1, decimo+r1, r1):
    print('{} '.format(c), end=' => ')
print('FIM')