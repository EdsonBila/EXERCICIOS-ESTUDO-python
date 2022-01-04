'''Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.'''
salario = int(input('Digite o salario '))
percentual = int(input('Digite o percentual '))
aumento = salario * percentual / 100
print('Valor do almento ',aumento)
novo_salario = salario + aumento
print('Seu novo salario ',novo_salario)
