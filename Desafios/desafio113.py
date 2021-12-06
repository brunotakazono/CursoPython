def leiaInt(msg):
    while True:
        try:
            valorint = int(input(msg))
            return valorint
        except (ValueError, TypeError):
            print('\nERRO! Informe um valor INTEIRO corretamente...')
        except KeyboardInterrupt:
            print('\nO usuário não informou esse número...')
            return 0


def leiaFloat(msg):
    while True:
        try:
            valorfloat = float(input(msg))
            return valorfloat
        except (ValueError, TypeError):
            print('ERRO! Informe um valor FLUTUANTE corretamente...')
        except KeyboardInterrupt:
            print('O usuário não informou esse número...')
            return 0


int = leiaInt('Digite um valor inteiro: ')
float = leiaFloat('Digite um valor flutuante: ')

print(f'Você digitou como valor inteiro o número: {int} e como valor flutuante o número: {float}')