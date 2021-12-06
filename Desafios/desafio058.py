import random

n = random.randint(0, 6)
# print(n)

escolhido = int(input('Faça sua tentativa de descobrir o numero: '))
tent = 1
while escolhido != n:
    escolhido = int(input('Faça sua tentativa de descobrir o numero: '))
    if escolhido != n:
        tent += 1
    else:
        tent = tent + 1

print(f'Foram necessárias {tent} palpites para vencer!')
