pessoas = {}
cadpessoas = []
somaidtot = totpessoa = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Digite o nome da pessoa: '))
    while True:
        pessoas['sexo'] = str(input('Digite o sexo da pessoa: [M/F] ')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoas['idade'] = int(input('Digite a idade da pessoa: '))
    cadpessoas.append(pessoas.copy())
    totpessoa += 1
    somaidtot += pessoas['idade']
    media = somaidtot / totpessoa
    while True:
        r = str(input('Deseja Continuar? [S/N]: '))
        if r in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if r == 'N':
        break

print(cadpessoas)

print(f'O total de pessoas cadastradas é {totpessoa}')
print(f'A média das pessoas cadastradas é {media:.2f}')
print('As mulheres cadastradas foram', end=' ')
for p in cadpessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('Lista de pessoas  cadastradas acima da média', end=' ')
for p in cadpessoas:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}', end='')
    print()
