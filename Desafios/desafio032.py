biss = int(input('Dgite o ano que deseja verificar se e bissexto: '))

if (biss % 4 == 0) and (biss % 100  !=  0) or (biss % 400 == 0):
    print(f'O ano {biss} é bissexto')
else:
    print(f'O ano {biss} não e bissexto')
