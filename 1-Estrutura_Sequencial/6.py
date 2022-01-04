'''Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber, sabendo-se que o funcionário tem graticação de 5% sobre o salário base e paga imposto de 7% também sobre o salário base.'''
salario1 = int(input('Digite o salario base '))
gratificacao = salario1 * 5 / 100
imposto = salario1 * 7 / 100
receber = salario1 + gratificacao - imposto
print('Salario a receber ',receber)