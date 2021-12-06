def aumentar(n, x, m=False):
    res = n + (n * x / 100)
    if m is False:
        return res
    else:
        return moeda(res)


def diminuir(n, x, m=False):
    res =  n - (n * x / 100)
    if m is False:
        return res
    else:
        return moeda(res)

def dobro(n, m=False):
    res = n * 2
    if m is False:
        return res
    else:
        return moeda(res)


def metade(n, m=False):
    res = n / 2
    if m is False:
        return res
    else:
        return moeda(res)


def moeda(n=0, m='R$'):
    return f'{m} {n:.2f}'.replace('.', ',')
