kmp = float(input('Qual foi a quantidade de KM percorridos?: '))
qtdd = float(input('Qual foi a quantidade de dias pela qual foi alugado?: '))


pp = (qtdd * 60) + (kmp * 0.15)


print(f'Foram percorridos {kmp} nos {qtdd} dias alugado(s) e o preço a pagar é R$ {pp:.2f}')
            
