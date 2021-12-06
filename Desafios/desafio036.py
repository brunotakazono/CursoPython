valcas = float(input('Qual o valor da casa que quer financiar?: '))
sal = float(input('Qual seu sálario? :'))
tmp = float(input('Em quantos anos pretende pagar?: '))
apm = tmp*12
presm = valcas / (apm)

if presm > sal*0.3:
    print('Empréstimo negado infelizmente você não pode financiar essa casa')
elif presm <= sal*0.3:
    print('Emprestimo Aprovado')
    print(f'Empréstimo aprovado a sua prestação mensal será de {presm:.2f} dividido em {apm:.0f} meses')