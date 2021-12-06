n = int(input('Digite um numero: '))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        total += 1
if total == 2:
    print('O número digitado é primo! ')
else:
    print('O número digitado não é primo')
