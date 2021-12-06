s = count = 0
while True:
    n = int(input('Digite um numero inteiro e 999 para parar: '))
    if n == 999:
        break
    if n != 999:
        s += n
        count += 1

print(f'Foram digitados {count} numeros!')
print(f'A soma dos numeros digitados é : {s} ')
