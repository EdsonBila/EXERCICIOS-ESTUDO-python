'''Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo.'''

n = int(input('Digite um número inteiro: '))
if n%2 > 0:
    print('Impar')
elif n == 0:
    print('Impar')
else:
    print('Par')
if n > 0:
    print('Positivo')
elif n == 0:
    print('Nulo')
else:
    print('Negativo')
