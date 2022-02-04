def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(preco)


def diminui(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(preco)


def dobr(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(preco)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(preco)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')