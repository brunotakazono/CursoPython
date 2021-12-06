frase = str(input('Digite uma frase :')).strip().upper()
palavras = frase.split()
juntapal = ''.join(palavras)
invpal = ''

for c in range(len(juntapal)-1, -1, -1):
    invpal += (juntapal[c])

if invpal == juntapal:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo')