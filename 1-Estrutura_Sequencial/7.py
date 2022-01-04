'''Faça um programa que receba o salário base de um funcionário, calcule e mostre seu salário a receber, sabendo-se que o funcionário tem graticação de 50,00 sobre o salário base e paga imposto que deve ser lido e é aplicado sobre o salário base.'''
salarioBase = float(input("Digite o Salário Base: "))
perImposto = float(input("Digite o Imposto: "))
imposto = salarioBase * perImposto / 100
salario_a_receber = salarioBase + 50 - imposto
print(' Salário a receber R$:',salario_a_receber)
