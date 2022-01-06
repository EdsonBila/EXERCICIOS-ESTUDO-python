'''Faça um algoritmo que calcule e exiba o salário reajustado de um funcionário de acordo com a seguinte regra: Salário até 300, reajuste de 50%; Salários maiores que 300, reajuste de 30%.'''

s = float(input('Informe o salário: '))
if s <= 300:
    ns = s + (s * 50 / 100)
    print('Reajuste de 50%: ',ns)
else:
    ns = s + (s * 30 / 100)
    print('Reajuste de 30%: ',ns)