counti = 0
counth = 0
countmm20 = 0
while True:
    idade = int(input('Digite a idade da pessoa a ser cadastrada: '))
    sexo = str(input('Digite o sexo da pessoa a ser cadastrada [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa a ser cadastrada [M/F]: ')).strip().upper()[0]
    if idade > 18:
        counti += 1
    if sexo == 'M':
        counth += 1
    if sexo == 'F' and idade < 20:
        countmm20 += 1
    escolha = str(input('Quer Continuar ? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Quer Continuar ? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        print('VAMOS AOS RESULTADOS')
        break

print(f'A quantidade de pessoas com mais de 18 anos é {counti}')
print(f' A quantidade de homens que foram cadastrados é {counth}')
print(f'A quantidade de mulheres com menos de 20 anos é {countmm20}')
