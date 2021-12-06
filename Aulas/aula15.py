""" Estruturas de repetição pt3  interrompendo repetições"""

# cont = 1
# while cont <= 10:
#     print(cont, '→ ', end='')
#     cont += 1
# print('Acabou')

# cont = 1
# while True:
#     print(cont, '→ ', end='')
#     cont += 1
# print('Acabou')

# n = cont = 0
# while cont < 3:
#     n = int(input('Digite um numero : '))
#     cont += 1

# n = s = 0
# while n != 999:
#     n = int(input('Digite um numero: '))
#     s += n
# print(f'A soma vale {s}')

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n

print(f'A soma vale {s}')
