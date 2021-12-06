lista = []
listapar = []
listaimpar = []
while True:
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    choose = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if choose in 'Nn':
        break

print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de impares é {listaimpar}')
