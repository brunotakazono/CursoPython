lista = []

while True:
        lista.append(int(input('Digite um valor: ')))
        print('Adicionado com sucesso...')
        choose = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if choose in 'Nn':
            break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente {lista}')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não esta na lista!')
