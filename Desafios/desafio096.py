def area(largura, comprimento):
    retarea = largura * comprimento
    print(f'A área do retangulo deo seu terreno de {largura} x {comprimento} é {retarea} m²')


def titulo(txt):
    print(txt)



titulo('CONTROLE DE TERRENOS')
print('-' * 30)
largura = int(input('Largura (m): '))
comprimento = int(input('Comprimento (m): '))
area(largura, comprimento)
