import datetime
anoatual = datetime.date.today().year
anonasc = int(input('Digite o ano de nascimento do atleta: '))
idade = anoatual - anonasc

if idade <= 9:
    print('Atleta pertence a categoria MIRIM.')
elif 9 < idade <= 14:
    print('Atleta pertence a cateforia INFANTIL.')
elif 14 < idade <= 19:
    print('Atleta pertence a categoria JUNIOR.')
elif 19 < idade <= 20:
    print('Atleta pertence a categoria SENIOR.')
elif idade > 20:
    print('Atleta pertence a categoria MASTER.')