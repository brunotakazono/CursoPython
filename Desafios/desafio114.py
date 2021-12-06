import requests
try:

    url = 'http://www.pudim.com.br/'
    response = requests.get(url)

    print(f'\n{" CONEXÃO REALIZADA ":-^43}')
    print('Parece que você CONSEGUIU entrar no site...')
    print(f'URL: {url}'.center(43))
    print('-' * 43 + '\33[m')
except requests.ConnectionError:
    print(f'\n{" ERRO ":-^47}')
    print(f'Parece que você NÃO CONSEGUIU entrar no site...\n{"Tente mais tarde!".center(45)}')
    print('-' * 47 + '')