def aumentar(p, v):
    """
    :param p: preço
    :param v: porcentagem a ser aumentada
    """
    return ((p / 100) * v) + p


def diminuir(p, v):
    """
    :param p: preço
    :param v: porcentagem a ser reduzida
    """
    return p - ((p / 100) * v )


def dobro(v):
    return v * 2


def metade(v):
    return v / 2


def moeda(v):
    return f'R${v:.0f},00'

