def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return res


def diminui(preco, taxa):
    res = preco - (preco * taxa/100)
    return res


def dobr(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res