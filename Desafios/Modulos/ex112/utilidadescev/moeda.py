def aumentar(n, x, m=False):
    res = n + (n * x / 100)
    if m is False:
        return res
    else:
        return moeda(res)


def diminuir(n, x, m=False):
    res = n - (n * x / 100)
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


def titulo(msg):
    print('-' * 35)
    print(msg)
    print('-' * 35)


def resumo(n, x, y):
    titulo(f'{"RESUMO DO VALOR":^30}')
    print(f'Preço analisado:\t{moeda(n)}')
    print(f'Dobro do preço:\t\t{dobro(n, True)}')
    print(f'Metade do preço\t\t{metade(n, True):}')
    print(f'{x}% de aumento:\t\t{aumentar(n, x, True)}')
    print(f'{y}% de redução:\t\t{diminuir(n, y, True)}')
    print('-' * 35)
