'''. Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo. Esse programa deverá calcular e mostrar a quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado.'''
custo = float(input('Custo: '))
convite = float(input('Valor do convite R$: '))
quantidade = custo / convite
print('Quantidade de convites vendidos: ',quantidade)