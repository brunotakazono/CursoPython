nome = str(input('Digite seu nome completo: '))
print('Muito prazer em te conhecer!')
          
separar  =  nome.split()
print(separar)

print('Seu primeiro nome é {}'.format(nome[9]))
print('Seu ultimo nome e {}'.format(separar[len(separar)-1]))
