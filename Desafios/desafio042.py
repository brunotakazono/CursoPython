r1 = int(input('Digite o primeiro lado: '))
r2 = int(input('Digite o seugndo lado: '))
r3 = int(input('Digite o terceiro lado: '))

if r1 < (r2+r3) and r2 < (r1+r3) or r3 <(r1+r2):
    print('Formam um triângulo.')
    if (r1 == r2) and (r1 == r3):
        print('O triângulo é Equilatero! ')
    elif r1 == r2 and (r3 != r1) or (r2 == r3) and (r1 != r3):
        print('O triângulo é Isosceles')
    elif (r1 != r2) and (r1 != r3) or (r2 != r3):
        print('O triângulo é Escaleno')