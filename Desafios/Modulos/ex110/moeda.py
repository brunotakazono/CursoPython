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
    print(f'{"Preço analisado:":<4}{moeda(n):>15}')
    print(f'{"Dobro do preço:":<4}{dobro(n, True):>17}')
    print(f'{"Metade do preço:":<4}{metade(n, True):>15}')
    print(f'{x}{"% de aumento:":<4}{aumentar(n, x, True):>16}')
    print(f'{y}{"% de redução:":<4}{diminuir(n, y, True):>16}')
    print('-' * 35)
