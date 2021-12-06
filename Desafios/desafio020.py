from random import shuffle

aluno1 = input('Digite o nome do aluno1: ')
aluno2 = input('Digite o nome do aluno2: ')
aluno3 = input('Digite o nome do aluno3: ')
aluno4 = input('Digite o nome do aluno4: ')

ordems = [aluno1, aluno2, aluno3, aluno4]
shuffle(ordems)

print(f'A ordem de apresentação é {(ordems)}.') 
