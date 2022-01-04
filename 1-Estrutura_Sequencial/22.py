'''Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. Faça um programa que receba o valor do salário mínimo e a quantidade de quilowatts consumida por uma residência. Calcule e mostre: o valor de cada quilowatt; o valor a ser pago por essa residência; o valor a ser pago com desconto de 15%'''
valor_do_salario = float(input('Informe o valor do salário: '))
quantidade_de_quilowatt = float(input('Informe a quantidade de Quilowatt: '))
valor_do_quilowatt = valor_do_salario / 5
valor_em_reais = valor_do_quilowatt * quantidade_de_quilowatt
valor_do_desconto = valor_em_reais * 15 / 100
valor_com_desconto = valor_em_reais - valor_do_desconto
print('O valor de cada quilowatt: ',valor_do_quilowatt)
print('O valor a ser pago por essa residência: ',valor_em_reais)
print('O valor a ser pago com desconto de 15%: ',valor_com_desconto)
