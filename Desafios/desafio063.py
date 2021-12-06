n = int(input('Quantos termo da sequencia de Fibonnaci você quer mostrar: '))
termo1 = 0
termo2 = 1

print(f'{termo1} → {termo2} ', end='')
count=3
while count <= n:
    termo3 = termo1 + termo2
    print(f' → {termo3} ', end='')
    termo1 = termo2
    termo2 = termo3
    count += 1
print(' → FIM ')