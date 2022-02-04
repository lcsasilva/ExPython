d = 0
for c in range(1, 501, 2):
    t = c % 3
    if t == 0:
        d = d + c
print('A soma de todos os valores é {}.'.format(d))