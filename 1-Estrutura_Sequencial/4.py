'''Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.'''
salario = int(input('Digite o salario '))
novo_salario = salario + (salario * 25 / 100)
print('Seu novo salario: ',novo_salario)
