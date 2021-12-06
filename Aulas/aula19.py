"""Dicionarios
listas:
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[1])
mas se eu quiser indices literais usa-se os dicionários


filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas' }

print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}')

locadora = []
"""

# pessoas = {'nome': 'Gustavo','sexo': 'M', 'idade': 22}
# print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# pessoas['peso'] = 98.5

# del pessoas['sexo']

# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil[1]['sigla'])

""""estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

"""