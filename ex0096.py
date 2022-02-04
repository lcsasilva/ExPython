print('Controle de Terrenos')
print('-'*40)

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))


def soma(a, b):
    s = a * b
    print(f'A área de um terreno {a}x{b} é de {s}m²')


soma(largura, comprimento)