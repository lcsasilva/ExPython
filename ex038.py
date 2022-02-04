num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print('O {} é maior que o {}.'.format(num1, num2))
elif num1 < num2:
    print('O {} é maior que o {}.'.format(num2, num1))
elif num1 == num2:
    print('Os valores são iguais!')
