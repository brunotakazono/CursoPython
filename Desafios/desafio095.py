from time import sleep

jogadorfut = {}
totgols = 0
partidas = []
gols = 0
time = []
while True:
    jogadorfut.clear()
    jogadorfut['nome'] = str(input('Digite o nome do jogador: '))
    totpart = int(input(f'Quantas partidas {jogadorfut["nome"]} participou: '))
    partidas.clear()
    for i in range(0, totpart):
        partidas.append(int(input(f'Quantos gols {jogadorfut["nome"]} fez na partida {i + 1}: ')))
        jogadorfut['gols'] = partidas[:]
        totgols = sum(partidas)
    jogadorfut['total de gols'] = totgols
    time.append(jogadorfut.copy())
    while True:
        r = str(input('Deseja Continuar? [S/N]: '))
        if r in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if r == 'N':
        break
print('-' * 50)
print(f'{"cod":<4} {"nome":>3} {"gols":>14} {"total":>15}')
for k, v in enumerate(time):
    print(f'{k:<4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
    print('-' * 50)
print(time)
while True:
    procura = int(input('Mostrar dados de qual jogador? (999) para parar : '))
    if procura == 999:
        print('<< VOLTE SEMPRE >>')
        sleep(2)
        break

    if procura >= len(time):
        print(f'Erro não existe jogador com cod {procura}!')
    else:
        print(f'-- LEVANTAMENTO DE JOGADOR {time[procura]["nome"]}:')
        for c, p in enumerate(time[procura]["gols"]):
            print(f'No jogo {c + 1}, fez {p} gols.')
