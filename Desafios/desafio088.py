import random
from time import sleep

print('-' * 30)
print(f"{'JOGA NA MEGA SENA':^30}")
print('-' * 30)

jogos = int(input('Quantos jogos você quer que eu sorteie?: '))

for num in range(0, jogos):
    lista_aleatoria = random.sample(range(0, 100), 6)
    print(f'Jogo {num + 1}: {lista_aleatoria}')
    sleep(2)
print('-=' * 5, '< Boa Sorte! >', '-=' * 5)
