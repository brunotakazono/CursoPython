dist = float(input('Informe a distancia da viagem em KM: '))

if dist <= 200:
    preco = dist*0.50
    print(f'O preço a pagar é R$ {preco:.2f}')
else:
    preco = dist*0.45
    print(f'O preço a pagar é R$ {preco:.2f}')
    
