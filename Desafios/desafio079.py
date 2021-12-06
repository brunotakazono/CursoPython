lista = []

while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Adicionado com sucesso...')
        choose = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    else:
        print('Valor duplicado! Não adicionar...')
        choose = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if choose in 'Nn':
            break
        else:
            choose = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
print(f'Você digitou os valores {sorted(lista)}')
