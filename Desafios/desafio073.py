g20 = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Bragantino', 'Fortaleza', 'Fluminense',
       'Ceará', 'Internacional', 'América-MG', 'Santos', 'São Paulo', 'Atlético-GO', 'Cuiabá', 'Athletico-PR',
       'Bahia', 'Juventude', 'Grêmio', 'Sport', 'Chapecoense')

print(f'Os 5 primeiros colocados são {g20[:5]}')
print(f'Os 4 ultimos colocados sçao {g20[-4:]}')
print(f'Times em ordem alfabética {sorted(g20)}')
print(f'A chapecoense está na {g20.index("Chapecoense")+1}ª posição.')
