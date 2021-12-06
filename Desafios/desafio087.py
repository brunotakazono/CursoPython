matrix = [0, 0, 0], [0, 0, 0], [0, 0, 0]
somapar = 0
soma3c = 0
maiorval = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite o termo [{l},{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print('')

for l in range(0, 3):
    for c in range(0, 3):
        if matrix[l][c] % 2 == 0:
            somapar += matrix[l][c]
for l in range(0, 3):
    soma3c += matrix[l][2]
for c in range(0, 3):
    if matrix[1][c] == 0:
        maiorval = matrix[1][c]
    else:
        if maiorval < matrix[1][c]:
            maiorval = matrix[1][c]

print(f'A soma dos valores pares é : {somapar}')
print(f'A soma dos valores pares é : {soma3c}')
print(f'O maior valor da segunda linha é {maiorval}')
