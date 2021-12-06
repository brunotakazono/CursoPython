''' Manipulando strings
 -Fatiamento >>> frase[9] pega o caractere na posição 9
 -Analise >>> len() comprimento
              count() conta numero de ocorrencias
              find() mostra onde começou
              usar operador in ex curso in frase retorna booleana
-Transformação >>> replace() substitui string por outra
                   upper() substitui kinusculas em maiscula
                   lower() substitui maiusculas por minusculas
                   capitalize() pega string joga tudo pra minuscula
                   e só a primiera fica em maiuscula
                   title() Analisa quantas palavras e faz capitalize palavra por palavra
                   strip() remove todos os espaços inuteis do código
                   rstrip() remove os espaços a direita
                   lstrip() remove os espaços da esquerda
-Divisão           split()    divide string em uma lista
-Junção            .join() '''



#frase = ' Curso de Vídeo Python '
#print(frase[1::2])
#print(frase.upper().count('O'))
#print(len(frase.strip()))

frase = 'Curso em Vídeo Python'

print(frase.replace('Python', 'Android'))
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)                     


print(frase.find('Android'))
print(frase.lower().find('vídeo'))

dividido = frase.split()
print(dividido[0])
print(dividido[2][2])
