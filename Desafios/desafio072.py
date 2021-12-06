numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')


for ext in numeros:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        numext = numeros[n]
        print(f'Você digitou o número {numext}')
    else:
        print('Tente novamente.', end=' ')
        n = int(input('Digite um numero entre 0 e 20: '))