'''O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos, calcule e mostre: o valor correspondente ao lucro do distribuidor; o valor correspondente aos impostos; o preço nal do veículo'''
pr_fabrica = float(input('Preo de Fabrica: '))
pe_l_distribuidor = float(input('Percentual de Lucro do Distribuidor: '))
pe_imposto = float(input('Impostos: '))
lu_distribuidor = pr_fabrica * pe_l_distribuidor / 100
va_imposto = pr_fabrica * pe_imposto / 100
pr_final = pr_fabrica + lu_distribuidor + va_imposto
print('Lucro do distribuidor: ',lu_distribuidor)
print('Valor do imposto: ',va_imposto)
print('Preço Final: ',pr_final)