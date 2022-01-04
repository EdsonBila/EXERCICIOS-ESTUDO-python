'''Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo, calcule e mostre o salário a receber, seguindo estas regras: a hora trabalhada vale a metade do salário mínimo. o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada. o imposto equivale a 3% do salário bruto. o salário a receber equivale ao salário bruto menos o imposto.'''
quantidade_de_horas_trabalhadas = float(input('Número de horas trabalhadas: '))
valor_salario_minimo = float(input('Valor do salário mínimo: '))
valor_hora_trabalhada = valor_salario_minimo / 2
valor_salario_bruto = valor_hora_trabalhada * quantidade_de_horas_trabalhadas
impostos = valor_salario_bruto * 3 / 100
valor_salario_liquido = valor_salario_bruto - impostos
print('Seu salário líquido: ',valor_salario_liquido)
