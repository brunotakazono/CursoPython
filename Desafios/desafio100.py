import random

numeros = []
numerospar = []


def sorteia():
    for n in range(0, 5):
        sorteio = random.randint(0, 100)
        numeros.append(sorteio)
    print(f'Os numeros sorteados são {numeros}')


def somapar():
    spar = 0
    for valor in numeros:
        if valor % 2 == 0:
            numerospar.append(valor)
    spar += sum(numerospar)
    print(f'A soma dos  numeros pares {numerospar} é de {spar}.')


sorteia()
somapar()
