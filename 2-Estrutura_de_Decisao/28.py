'''Faça um programa que receba o salário base e o tempo de serviço de
um funcionário. Calcule e mostre:
O imposto, conforme a tabela a seguir.
A graticação, de acordo com a tabela a seguir.
O salário líquido, ou seja, salário base menos imposto mais graticação.
A categoria, que está na tabela a seguir.'''

salario_base = float(input('Informe o salário base: '))
tempo_servico = float(input('Informe o tempo de serviço: '))
if salario_base < 200:
    imposto = 0
elif salario_base <= 450:
    imposto = 3/100 * salario_base
elif salario_base < 700:
    imposto = 8/100 * salario_base
else:
    imposto = 12/100 * salario_base
print('Imposto: ',imposto)
if salario_base > 500:
    if tempo_servico <= 3:
         gratificacao = 20
    else: 
        gratificacao = 30
else:
    if tempo_servico <= 3:
        gratificacao = 23
    elif tempo_servico < 6:
        gratificacao = 35
    else:
        gratificacao = 33
print('Gratificação: ',gratificacao)
salario_liquido = salario_base - imposto + gratificacao
print('Salario liquido: ',salario_liquido)
if salario_liquido <= 350:
    print('Classificação A')
else:
    if salario_liquido < 600:
        print('Classificação B')
    else:
        print('Classificação C')
