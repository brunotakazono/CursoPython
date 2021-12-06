from random import randint
count = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR \n')
player = int(input('Diga um valor: '))
escolha = str(input('Par ou Ímpar? [P/I] '))
computador = randint(3, 10)
while True:
    s = player + computador
    if s % 2 == 0:
        res = 'DEU PAR'
    else:
        res = 'DEU IMPAR'
    print('-' * 20)
    print(f'Você jogou {player} e o computador jogou {computador}. Total de {s} {res} ')
    print('-' * 20)
    if res == 'DEU PAR' and escolha == 'P':
        print('Você VENCEU !')
        print('Vamos jogar novamente ...')
        player = int(input('Diga um valor: '))
        escolha = str(input('Par ou Ímpar? [P/I] '))
        count += 1
        print('-=' * 20)
    elif res == 'DEU IMPAR' and escolha == 'I':
        print('Você VENCEU !')
        print('Vamos jogar novamente ...')
        player = int(input('Diga um valor: '))
        escolha = str(input('Par ou Ímpar? [P/I] '))
        print('-=' * 20)
        count += 1
    else:
        print(f'GAME OVER! Você venceu {count} vezes.')
        break
