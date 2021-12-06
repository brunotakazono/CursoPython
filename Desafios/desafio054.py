import datetime
anoatual = datetime.date.today().year
s = 0
t = 0
for c in range(0, 7):
    anonasc = int(input('Digite o ano de nascimento: '))
    idade = anoatual - anonasc
    if idade < 18:
        s += 1
    elif idade >= 18:
        t += 1
print(f'O total de  adultos são {t} e os que não atingiram a maioridade são {s}')
