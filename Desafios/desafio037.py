num = int(input('Digite o numero a ser convertido: '))
choose = int(input('Escolha a opção \n'
                   '1- para bínario \n'
                   '2- para octal \n'
                   '3- para hexadecimal \n'))

if choose == 1:
    numbin = bin(num)
    print(f'O número {num} convertido em binário é {numbin} ')
elif choose == 2:
    numoct = oct(num)
    print(f' O número {num} convertido em octal é {numoct}')
elif choose == 3:
    numhex = hex(num)
    print(f'O número {num} convertido em hexadecimal é {numhex}')
