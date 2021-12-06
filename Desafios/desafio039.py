import datetime
anoatual = datetime.date.today().year
anonasc = int(input('Digite o ano de nascimento: '))
idade = anoatual - anonasc

alistamento = 18

if idade < alistamento:
    print('Ainda irá se alistar no serviço militar.')
    falta = alistamento - idade
    print(f'Você devera se apresentar para alistar em {falta} anos')
elif idade == alistamento:
    print('Está na hora de se alistar para o serviço militar.')
if idade > alistamento:
    print('Já passou do tempo de se alistar ao serviço militar.')
    passou = idade - alistamento
    print(f'Você passou {passou} anos do prazo de alistamento')