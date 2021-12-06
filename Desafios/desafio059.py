n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

print('-' * 20)
print('MENU')
print('-' * 20)
print('[1] Somar \n'
      '[2] multiplicar \n'
      '[3] marior \n'
      '[4] novos numeros \n'
      '[5] sair do programa \n')

op = int(input('Digite a opção:'))
while op != 5:
    if op == 1:
        s = n1 + n2
        print(f'A soma é : {s}')
        op = int(input('Digite a opção:'))
    elif op == 2:
        m = n1 * n2
        print(f'A multipilixação é: {m}')
        op = int(input('Digite a opção:'))
    elif op == 3:
        if n1 > n2:
            print(f'O primeiro numero {n1} digitado é o maior!')
            op = int(input('Digite a opção:'))
        else:
            print(f'O segundo numero digitado {n2} é o maior!')
            op = int(input('Digite a opção:'))
    elif op == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        op = int(input('Digite a opção:'))
