import moeda
from moeda import moeda as md

p = float(input('Digite: '))

print(f'A metade de {p} é {md(moeda.metade(p))}')
print(f'O dobro de {p} é {md(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {md(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {md(moeda.diminuir(p, 13))}')
