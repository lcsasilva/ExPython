from datetime import date
ano = date.today().year
menor = 0
maior = 0
for pessoas in range(1, 7):
    idade = int(input('Em que ano a {}° pessoa nasceu?: '.format(pessoas)))
    idade2 = ano - idade
    if idade2 >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas ainda não atingiram a maioridade e {} são maiores!'.format(
    menor, maior
))
