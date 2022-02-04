n1 = int(input('Digite a primeira medida: '))
n2 = int(input('Digite a segunda medida: '))
n3 = int(input('Digite a terceira medida: '))

lista = [n1, n2, n3]
lista.sort()

if lista[-1] < lista[0]+lista[1]:
    print('É possível montar um triângulo!')
else:
    print('Não é possível montar um triângulo!')