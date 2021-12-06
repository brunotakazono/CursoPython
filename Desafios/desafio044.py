prod = float(input('Digite o preço do produto em R$: '))
formpag = int(input('Digite a forma de pagamento: \n'
                    '1- À vista dinheiro/cheque: \n'
                    '2- Á vista no cartão: \n'
                    '3- Em até 2x no cartão: \n'
                    '4- 3x ou mais no cartão: \n'))
if formpag == 1:
    valorpag = prod - (prod * 0.1)
    print(f'O valor a ser pago pelo produto é R$ {valorpag:.2f}')
elif formpag == 2:
    valorpag = prod - (prod * 0.05)
    print(f'O valor a ser pago pelo produto é R$ {valorpag:.2f}')
elif formpag == 3:
    valorpag = prod

    print(f'O valor a ser pago pelo produto é R$ {valorpag:.2f}')
elif formpag == 4:
    valorpag = prod + (prod * 0.2)
    print(f'O valor a ser pago pelo produto é R$ {valorpag:.2f}')
