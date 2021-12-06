valores = []
maior =0
menor =0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Você digitou os valores {valores}')
print((f'O maior valor digitado {maior} '))
print(f'O menor valor digitado {menor}')
print(f'O mario valor é {max(valores)}')
print(f'O menor valor é {min(valores)}')

