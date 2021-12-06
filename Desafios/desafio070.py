totgasto = 0
maior1000 = 0
cn = 0
menor = 0
barato = ''
while True:
    nome = str(input('Digite nome do produto: '))
    preco = int(input('Digite preço do produto: '))
    escolha = str(input('Quer Continuar ? [S/N]: ')).strip().upper()[0]
    cn += 1
    totgasto += preco
    if preco > 1000:
        maior1000 += 1
    if cn == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    while escolha not in 'SN':
        escolha = str(input('Quer Continuar ? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        print('VAMOS AOS RESULTADOS')
        break

print(f'O total gasto é R$ {totgasto}')
print(f'O total de produto que custam mais que 1000 é {maior1000}')
print(f'O produto mais barato é {barato}')
