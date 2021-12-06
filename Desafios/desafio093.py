jogadorfut = {}
totgols = 0
partidas = []
gols = 0
jogadorfut['nome'] = str(input('Digite o nome do jogador: '))
totpart = int(input(f'Quantas partidas {jogadorfut["nome"]} participou: '))
for i in range(0, totpart):
    partidas.append(int(input(f'Quantos gols {jogadorfut["nome"]} fez na partida {i + 1}: ')))
    jogadorfut['gols'] = partidas[:]
    totgols = sum(partidas)
jogadorfut['total de gols'] = totgols
print('-' * 50)
for k, v in jogadorfut.items():
    print(f'O campo {k} tem o valor {v}')
print('-' * 50)
print(f'O jogador {jogadorfut["nome"]} jogou {totpart} partidas ')
for c, p in enumerate(jogadorfut['gols']):
    print(f'=> Na partida {c + 1}, fez {p} gols.')
print(f'Foi um total de {jogadorfut["total de gols"]} gols.')
