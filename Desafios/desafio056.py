mediaid = 0
mulhermeno20 = 0
nomehvelho = ''
hmaisvelho = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa: '))
    mediaid += idade / 4
    if c == 1:
        if sexo == 'M':
            hmaisvelho = idade
            nomehvelho = nome
        if (sexo == 'F') and (idade < 20):
            mulhermeno20 += 1
    else:
        if (sexo == 'M') and (hmaisvelho < idade):
            hmaisvelho = idade
            nomehvelho = nome
        else:
            nomehvelho = 'não existe homens'
        if (sexo == 'F') and (idade < 20):
            mulhermeno20 += 1
print(f'A média da idade do grupo é: {mediaid}')
print(f'O nome do homem mais velho é: {nomehvelho}')
print(f'O numero de mulheres de menos de 20 anos é : {mulhermeno20} ')
