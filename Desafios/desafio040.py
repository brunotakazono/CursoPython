nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota:'))

media = (nota1 + nota2) / 2

if media < 5:
    print('O aluno foi Reprovado')
elif 5 < media < 6.9:
    print('O aluno está de Recuperação')
elif media > 7:
    print('O aluno foi Aprovado')
