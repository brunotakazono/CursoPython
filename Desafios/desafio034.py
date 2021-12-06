sal = float(input('Digite o valor do salário em R$: '))

if sal > 1250:
    aumento = sal*0.1
if sal <= 1250:
    aumento = sal*0.15

novosal = sal + aumento    

print(f'O aumento sera de R$: {aumento:.2f} ')
print(f'O novo salário sera de R$ {novosal:.2f}')
            
