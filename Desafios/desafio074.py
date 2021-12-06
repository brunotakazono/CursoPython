from random import randint
tupla = (randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000))
# tupla = tuple(randint(i+1, 1000) for i in range(randint(5, 5)))
print(f'os valores sorteado foram: {tupla}')
for valores in tupla:
    print(f'O maior valor sorteado foi: {max(tupla)}')
    print(f'O menor valor sorteado foi: {min(tupla)}')
    break
