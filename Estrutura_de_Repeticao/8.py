'''Faça um algoritmo que calcule e exiba o salário reajustado de dez
funcionários de acordo com a seguinte regra:
    Salário até 300, reajuste de 50%;
    Salários maiores que 300, reajuste de 30%.'''
    
contador = 0
while contador <= 11:
    salario = float(input('Informe seu salário R$: '))
    if salario <= 300:
        reaj50 = salario + (salario*(50/100))
        print('Salário reajustado R$: ',reaj50)
    elif salario > 300:
        reaj30 = salario + (salario*(30/100))
        print('Salário reajustado R$: ',reaj30)
    contador = contador + 1