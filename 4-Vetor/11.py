'''Faça um programa que:
    preencha um vetor com seis elementos numéricos inteiros.
Calcule e mostre:
    todos os números pares;
    a quantidade de números pares;
    todos os números ímpares;
    a quantidade de números ímpares'''
    
n = []
npares = []
contpar = 0
nimpar = []
contimpar = 0
for i in range(6):
    n.append(int(input('Informe um número inteiro: ')))
    if n[i] % 2 == 0:
        npares.append(n[i])
        contpar += 1
    if n[i] % 2 != 0:
        nimpar.append(n[i])
        contimpar += 1
print('Da lista de números inteiros tem',contpar,'números pares, sendo eles:',npares)
print('Da lista de números inteiros tem',contimpar,'números impares, sendo eles:',nimpar)