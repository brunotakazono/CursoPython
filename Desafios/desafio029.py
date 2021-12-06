vel = float(input('Qual a velocidade?: '))

if vel > 80:
    multa = (vel - 80)* 7
    print (f'Você foi multado em R$ {multa:.2f}')
