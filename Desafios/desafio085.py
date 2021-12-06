numeros = [[], []]
for c in range(1, 8):
    valores = (int(input(f'Digite o {c}o valor: ')))
    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)
print(f'Os valores pares digitador foram: {sorted(numeros[0])}')
print(f'OS valores impares digitados foram: {sorted(numeros[1])}')