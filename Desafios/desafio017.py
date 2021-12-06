from math import hypot

ca = float(input('Digite o cateto adjacente: '))
co = float(input('Digite o cateto oposto: '))
hyp = hypot(ca, co)

print(f'A hipotenusa de um triângulo retangulo de cateto oposto {co}', end=' ')
print(f'e cateto adjacente {ca} é {hyp}')
