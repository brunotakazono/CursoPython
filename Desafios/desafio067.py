while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n > 0:
        print('-' * 20)
        for c in range(1, 11):
            print(f' {n} x {c:2} = {n * c}')
        print('-' * 20)
    elif n < 0:
        print('PROGRAMA TABUADA ENCERRADO!')
        break
