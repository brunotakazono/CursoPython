# from ex107 import moeda

# p = float(input('Digite o preço: R$ '))
# print(f'A metade de {p} é {moeda.metade(p)}')
# print(f'O dobro de {p} é {moeda.dobro(p)}')
# print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
# print(f'Reduzindo 13% temos {moeda.diminuir(p, 13)}')


# from ex108 import moeda

# p = float(input('Digite o preço: R$ '))
# print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
# print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
# print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
# print(f'Reduzindo 13% temos {moeda.moeda(moeda.diminuir(p, 13))}')

# from ex109 import moeda


# p = float(input('Digite o preço: R$ '))
# print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
# print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
# print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
# print(f'Reduzindo 13% temos {moeda.diminuir(p, 13, True)}')

# from ex110 import moeda

# from ex111.utilidadescev import moeda
# p = float(input('Digite o preço: R$ '))
# moeda.resumo(p, 80, 35)

from ex112.utilidadescev import dado
from ex112.utilidadescev import moeda

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 35, 22)
