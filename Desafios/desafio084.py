pessoas = list()
dado = list()
maispes = maislev = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maislev = maispes = dado[1]
    else:
        if dado[1] > maispes:
            maispes = dado[1]

        if dado[1] < maislev:
            maislev = dado[1]

    pessoas.append(dado[:])
    dado.clear()
    r = str(input('Quer continuar [S/N]'))
    if r in 'Nn':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print('\n')
print(f'O maior peso foi  de {maispes}.', end='')
for p in pessoas:
    if p[1] == maispes:
        print(f'{p[0]}', end='')
print('')
print(f'O menor peso foi  de {maislev}.', end='')
for p in pessoas:
    if p[1] == maislev:
        print(f'{p[0]}', end='')