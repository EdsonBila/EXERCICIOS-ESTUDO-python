'''Faça um programa que:
    Receba dez números inteiros e armazene-os em um vetor
    Armazene os numeros em dois vetores, um com números pares e o outro com os ímpares'''
    
n = []
npares = []
nimpar = []

for i in range(10):
    n.append(int(input('Informe um número: ')))
    if n[i] % 2 == 0:
        npares.append(n[i])
    if n[i] % 2 != 0:
        nimpar.append(n[i])
print('Na lista de números inteiros tem os números pares, sendo eles:',npares)
print('Na lista de números inteiros tem os números impares, sendo eles:',nimpar)