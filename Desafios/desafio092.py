import datetime

anoatual = datetime.datetime.today().year
trabalhador = {}

trabalhador['nome'] = str(input('Digite o nome do trabalhador: '))
trabalhador['ano de nascimento'] = int(input(f'Digite o ano de nacimento de {trabalhador["nome"]}: '))
trabalhador['idade'] = anoatual - trabalhador['ano de nascimento']
trabalhador['CTPS'] = int(input(f'Digite o número da CTPS do trabalhador: '))
if trabalhador['CTPS'] != 0:
    trabalhador['ano de contratação'] = int(input(f'Digite o ano de contratação de {trabalhador["nome"]}: '))
    trabalhador['salário'] = float(input(f'Digite o salário em R$ do trabalhador {trabalhador["nome"]}: '))
    aposentar = anoatual - trabalhador['ano de contratação']
    if aposentar >= 20:
        print('Já era pra estar aposentado')
    else:
        faltaaposentar = 20 - aposentar
        trabalhador['aposentar'] = trabalhador['idade'] + faltaaposentar
print(trabalhador)

for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
