from datetime import date

anoatual = date.today().year
anonasc = int(input('Em que ano você nasceu? : '))


def voto():
    idade = anoatual - anonasc
    if 18 <= idade < 70:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    if 16 <= idade < 18 or idade > 70:
        print(f'Com {idade} anos: VOTO OPCIONAL.')


voto()
