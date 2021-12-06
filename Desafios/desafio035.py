r1 = int(input('Digite o primeiro lado: '))
r2 = int(input('Digite o sefundo lado: '))
r3 = int(input('Digite o terceiro lado: '))

if r1 < (r2+ r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Podem formar um triângulo!')
else:
    print('Não podem formar um triângulo!')
