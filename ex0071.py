print('='*20)
print('BANCO CEV')
print('='*20)
cinquenta = vinte = dez= um = 0
valor = int(input('Que valor você quer sacar? R$'))
while True:
    while valor >= 50:
        valor -= 50
        cinquenta +=1
    while valor >= 20:
        valor -= 20
        vinte += 1
    while valor >= 10:
        valor -= 10
        dez += 1
    while valor >= 1:
        valor -= 1
        um += 1
    if valor == 0 or valor < 0:
        break
print(f'Total de {cinquenta} cédulas de R$50')
print(f'Total de {vinte} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {um}cédulas de R$1')
