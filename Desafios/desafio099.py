def maior(* valores):
    cont = maiorv = 0
    print('-=' * 30)
    print('Analisando os valores passados ....')
    for valor in valores:
        print(f'{valor} ', end='', flush=True)
        if cont == 0:
            maiorv = valor
        else:
            if valor > maiorv:
                maiorv = valor
        cont += 1
    print(f'Foram informados {cont} valores ')
    print(f'O maior valor é de {maiorv}')
    print('-=' * 30)



maior(3, 5, 7, 9)