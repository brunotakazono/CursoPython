valores = (int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')))
cont4 = valores.count(4)
print(f'O numero de vezes que o valor 4 aparece é {cont4}')

if valores == 3:
    print(f'O primeiro numero 3 foi digitado na {valores.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi dgitado em nenhuma posição')
print(f'Os numeros pares sao', end=' ')
for par in valores:
    if par % 2 == 0:
        print(par, end=' ')
