import random

pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'

jokenpo = [pedra, papel, tesoura]
jogador = str(input('Digite pedra papel ou tesoura para começar: '))
computador = random.choice(jokenpo)
print(computador)

if jogador == 'pedra' and computador == papel:
    print('Papel  ganha de pedra o jogador ganhou!')
elif computador == pedra and jogador == 'papel':
    print('Papel  ganha de pedra o computador ganhou!')
elif jogador == 'pedra' and computador == tesoura:
    print('Pedra ganha de tesoura  o jogador ganhou!')
elif computador == pedra and jogador == 'tesoura':
    print('Pedra ganha de tesoura o computador ganhou!')
elif jogador == 'pedra' and computador == pedra:
    print('Os dois jogaram pedra foi um empate!')
elif jogador == 'tesoura' and computador == papel:
    print('Tesoura ganha de papel o jogador venceu!')
elif computador == tesoura and jogador == 'papel':
    print('Tesoura ganha de papel computador venceu!')
elif computador == tesoura and jogador == 'tesoura':
    print('Os dois jogaram tesoura deu empate!')
elif computador == papel and jogador == 'papel':
    print('Os dois jogaram papel foi um empate!')
