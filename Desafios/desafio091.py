import random

jogadas = {'jogador1': random.randint(1, 6),
           'jogador2': random.randint(1, 6),
           'jogador3': random.randint(1, 6),
           'jogador4': random.randint(1, 6)}

ranking = list()
print('Valores sorteados:')
for k, v in jogadas.items():
    print(f'O jogador {k} tirou: {v}:')
print('Ranking dos jogares:')

ranking = sorted(jogadas.items(), key=lambda x: x[0])

for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar {v[0]} com {v[1]}')
