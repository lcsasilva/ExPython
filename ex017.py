from math import hypot

c_oposto = int(input("Digite o cateto oposto: "))
c_adj = int(input('Digite o cateto adjacente: '))

print('O cateto oposto tem o comprimento de {}, \n'
      'e o cateto adjacente tem {}, \n'
      'então a hipotenusa possuí {}! '.format(c_oposto, c_adj,
                                              hypot(c_oposto,c_adj)))