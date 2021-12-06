def aumentar(n, x):
    return n + (n * x / 100)


def diminuir(n, x):
    return n - (n * x / 100)


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def moeda(n=0, m='R$'):
    return f'{m} {n:.2f}'.replace('.', ',')
