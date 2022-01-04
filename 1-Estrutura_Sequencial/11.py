'''Faça um programa que receba um número positivo e maior que zero, calcule e mostre: O número digitado ao quadrado, O número digitado ao cubo, A raiz do número digitado, A raiz cúbica do número digitao'''
numero = int(input('Digite um numero: '))
quadrado = numero ** 2
cubo = numero ** 3
raiz_quadrada = round (numero ** (1/2))
raiz_cubica = round (numero ** (1/3))
print('O número digitado ao quadrado: ',quadrado)
print('O número digitado ao cubo: ',cubo)
print('A raiz do número digitado: ',raiz_quadrada)
print('A raiz cúbica do número digitado: ',raiz_cubica)
