'''Faça um programa que receba o salário inicial de um funcionário, calcule
e mostre o novo salário, acrescido de bonicação e de auxílio escola.
SALÁRIO                 | BONIFICAÇÃO
Até 500,00              | 5% do salário
Entre 500,00 e 1.200,00 | 12% do salário
Acima de 1.200,00       | Sem bonicação

SALÁRIO         | AUXÍLIO ESCOLA
Até 600,00      | 150,00
Acima de 600,00 | 100,00'''

s = float(input('digite o salário inicial R$:'))
if s <= 500:
    b = s * 5 / 100
    a_e = 150
elif 500 < s <= 1200:
    b = s * 12 / 100
    if s <= 600:
        a_e = 150
    else:
        a_e = 100
else:
    b = 0
    a_e = 100
s_a = s + b + a_e
print('salario atualizado R$: ',s_a)