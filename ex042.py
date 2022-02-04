print('\033[31mQUAL TRIÃNGULO IRÁ FORMAR?\033[m')
l1 = int(input('Digite um número inteiro: '))
l2 = int(input('Digite outro número inteiro: '))
l3 = int(input('Digite um terceiro número inteiro: '))
lados = [l1, l2, l3]
lados.sort()
if lados[2] > lados[1] + lados[0]:
    print('Não é possível montar um triângulo com essas medidas!')
else:
    if l1 == l2 == l3:
        print('Com essas medidas é possível montar um triângulo '
              'Equilátero!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Com essas medidas é possível montar um triângulo '
              'Isósceles!')
    elif l1 != l2 != l3 != l1:
        print('Com essas medidas é possível montar um triângulo '
              'Escaleno!')