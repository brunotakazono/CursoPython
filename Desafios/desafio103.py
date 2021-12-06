def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols}  gol(s) no campeonato.')


print('-' * 30)
nome = (input('Nome do Jogador: '))
golf = (input('Número de Gols: '))

if golf.isnumeric():
    golf = int(golf)
else:
    golf = 0
if nome.strip() == '':
    ficha(gols=golf)
else:
    ficha(nome, golf)
