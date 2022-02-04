import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}')
print(f'O dobro de R${p:.2f} é R${moeda.dobr(p):.2f}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10):.2f}')
print(f'Diminuindo 10%, temos R${moeda.diminui(p, 10):.2f}')
