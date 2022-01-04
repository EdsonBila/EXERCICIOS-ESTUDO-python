'''Faça um programa que receba um número real, encontre e mostre: a parte inteira desse número; a parte fracionária desse número; o arredondamento desse número. '''
numero = float(input('Digite um número real: '))
parte_inteira = numero // 1
parte_fracionaria = numero - parte_inteira
numero_arredondado = round(numero)
print('Parte inteira do número: ',parte_inteira)
print('Parte fracionária do número: ',parte_fracionaria)
print('O arredondamento do número: ',numero_arredondado)