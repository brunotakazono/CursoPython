import random

n = random.randint(0, 6)
#print(n)

escolhido = int(input('Faça sua tentativa de descobrir o numero: '))

if n == escolhido:
    print('você venceu!')
else:
    print('computador venceu!')
