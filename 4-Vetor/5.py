''' Faça um programa que carregue um vetor de oito elementos numéricos
inteiros, calcule e mostre os números pares e suas respectivas posições.'''

numerosint = []
for i in range(8):
    numerosint.append(int(input('Informe um número inteiro: ')))
    if numerosint[i] % 2 == 0:
        print('O número é par, com a posição',i)
        print('____________________________________')
    else:
        print('O NÚMERO NÃO É PAR')