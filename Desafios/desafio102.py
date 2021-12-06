def fatorial(n, show=False):
    """
    fatorial(n, show=False)
        -> Calcula o Fatorial de um número.
        :param n: O número a ser calculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número n
    """
    if n < 0:
        print("Factorial of negative num does not exist")

    elif n == 0:
        return 1

    else:
        fact = 1
        if show:
            for n in range(n, 0, -1):
                print(n, end=' ')
                if n > 1:
                    print('x', end=' ')
                else:
                    print('=', end=' ')
        while n > 1:
            fact *= n
            n -= 1
        return fact


fatorial(5, show=True)
help(fatorial)
