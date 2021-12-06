from time import sleep


def linha():
    print('-=' * 30)

    print()


def contador(i, f, p):
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p = p * -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont < f:
            print(f'{cont}', end=' ')
            cont += p
            sleep(0.3)
        print('FIM!', end='')
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
            sleep(0.3)
        print('FIM!', end='')
        print()



contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é a sua vez de personalizar a sua contagem!')
i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))

contador(i, f, p)
