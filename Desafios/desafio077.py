palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'prticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for sent in palavras:
    print(f'\nNa palavra {sent.upper()} temos ', end=' ')
    for letra in sent:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
