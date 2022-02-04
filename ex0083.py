exp = str(input('Digite a expressão: '))

a1 = exp.count('(')
a2 = exp.count(')')

if a1 != a2:
    print('Sua expressão está inválida!')
else:
    print('Sua espressão está válida.')