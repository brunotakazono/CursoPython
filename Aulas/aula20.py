"""Funções """

# def titulo(txt):
#    print('-' * 30)
#    print(txt)
#    print('-' * 30)


# titulo('  CURSO EM VIDEO  ')
# def soma():
#    a = int(input('Digite um numero:'))
#    b = int(input('Digite um numero:'))
#    return a + b

# print(soma())

# def soma(a, b):
#     print(f'A = {a} e b = {b}')
#     s = a + b
#     print(f'A soma de A + B = {s}')


# soma(4, 5)

# def contador(*núm):
#     for valor in núm:
#         print(f'{valor} ', end='')
#     print('FIM!')
# tam = len(núm)
# print(f'Recebi os valore {núm} e são ao todo {tam} números')


# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)


valores = [6, 3, 9, 1, 0, 2]


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


dobra(valores)
print(valores)
