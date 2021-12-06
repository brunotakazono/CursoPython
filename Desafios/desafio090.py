aluno = {}


aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print(f' O nome do aluno {aluno["nome"]}')
print(f' A média do aluno {aluno["média"]}')
print(f' A situação do aluno {aluno["situação"]}')