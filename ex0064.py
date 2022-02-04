cont = soma = 0
num = int(input('Digite um número inteiro:\n'
                '[999] para parar.'))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número inteiro:\n'
                    '[999] para parar.'))
print('Você digitou {} números e a soma de todos é {}.'.format(
    cont, soma
))
