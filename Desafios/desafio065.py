n = int
r = 'S'
m = s = cn = 0
maior = 0
menor = 0
while r != 'N':
    n = int(input('Digite um numero: '))
    r = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    s += n
    cn += 1
    m = s / cn
    if cn == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'A média é {m}')
print(f'O maior numero  digitado é {maior} e o menor numero digitado é {menor}')
