aluno = list()
while True:

    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    aluno.append([nome, [nota1, nota2], media])
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break

print('-=' * 30)
print(f"{'No':<5}{'Nome':>5}{'MÉDIA':>10}")
print('-' *15)
for i, a in enumerate(aluno):
    print(f'{i:<5}{a[0]:>5}{a[2]:>10}')
print('-' *15)
while True:
    mnota = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mnota == 999:
        break
    for i, a in enumerate(aluno):
        if mnota == i:
            print(f'As notas de {a[0]} são {a[1]}')

