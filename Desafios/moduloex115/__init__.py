def menu():
    from time import sleep
    print('-' * 40 + f'\n{" MENU ":^40}\n' + '-' * 40)  # Impressão do cabeçalho do Menu
    print('1- Ver pessoas cadastradas')
    print('2- Cadastrar nova pessoa')
    print('3- Sair do sistema')
    print('-' * 40)
    try:
        op = int(input('Sua Opção:'))
    except (ValueError, TypeError):
        print('\nERRO! Opção não existe. Tenta novamente...')
    else:
        if op == 1:
            sleep(1)
            listar_cadastros()
        elif op == 2:
            sleep(1)
            cadastrar()
        elif op == 3:
            sleep(1)
            finalizar()
        else:
            print('\nERRO! Opção não existe. Tente novamente...')


def listar_cadastros():
    print('\n' + '-' * 40 + f'\n{" PESSOAS CADASTRADAS ":^40}\n' + '-' * 40)

    arq_dados = open('moduloex115/database.txt', 'r', encoding='utf-8')

    print(f'{"NOME":<34}{"IDADE":^6}\n')
    for linha in arq_dados.readlines():
        dados = linha.split()

        nome = ' '.join(dados[:-1])
        idade = dados[-1]

        print(f'{nome:<34}{idade:^6}')
    print('-' * 40 + '\n')
    arq_dados.close()


def cadastrar():
    import time

    print('\n' + '-' * 40 + f'\n{" CADASTRAR PESSOA ":^40}\n' + '-' * 40)  # Impressão do cabeçalho

    arq_dados = open('moduloex115/database.txt', 'a', encoding='utf-8')  # Modo de escrita sem excluir conteúdo
    while True:
        try:
            nome = input('NOME: ').title().strip()
            idade = int(input('IDADE:'))
        except (ValueError, TypeError):
            print('\nERRO! Dados inválidos. Tente novamente...')
            continue

        arq_dados.write(nome + ' ' + str(idade) + '\n')  # Formato padrão: fulano de tal 35\n

        print('-' * 40)

        novo_cad = input('Novo cadastro ? [S/N]: ').upper().strip()
        while novo_cad not in ('S', 'N'):
            print('\nERRO! Opção não existe.')
            novo_cad = input('Novo cadastro? [S/N]: ').upper().strip()

        print('-' * 40)
        print('Salvo Com Sucesso!')
        print('-' * 40)

        if novo_cad == 'S':
            time.sleep(2)
            continue
        else:
            print('Encerrando cadastro(s). . .\n')
            time.sleep(2)
            break

    arq_dados.close()


def finalizar():
    from time import sleep
    print('-' * 40)
    print('Finalizando. . .\n')
    sleep(3)
    exit(0)
