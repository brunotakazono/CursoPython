s = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        s += c
print(f'A soma entre todos os números ímpares que são multiplos de de 3 indo de 1 até 500  3 é {s}')
