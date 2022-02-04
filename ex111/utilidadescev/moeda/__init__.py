def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if not formato else moeda(preco)


def diminui(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(preco)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(preco)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(preco)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')


def resumo(preco=0, txa=10, txr=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{txa}% de aumento: \t{moeda(aumentar(preco, txa))}')
    print(f'{txr}% de redução: \t{moeda(diminui(preco, txr))}')
    print('-'*30)
