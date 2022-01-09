'''Criar um algoritmo que leia dados para um vetor de 100 elementos
inteiros, imprimir o maior, o menor, o percentual de números pares e a média
dos elementos do vetor. Obs.: percentual = quantidade contada * 100 /
quantidade total. Não devem utilizar as funções: min(), max() e sum().'''

Ninteiros = []
maior = 0
menor = 10000
somaNpares = 0
somaNinteiros = 0
media = 0
for i in range(10):
    Ninteiros.append(int(input(f'Informe o {i + 1}º número: ')))
    if Ninteiros[i] >= maior:
        maior = Ninteiros[i]
    if Ninteiros[i] < menor:
        menor = Ninteiros[i]
    if Ninteiros[i] % 2 == 0:
        somaNpares += Ninteiros[i]
percentual = somaNpares * (100/10)
for i in Ninteiros:
    somaNinteiros += i
media = somaNinteiros / 10
print('O maior número é: ',maior)
print('O menor número é: ',menor)
print('O percentual de números pares é: ',percentual)
print('Média dos elementos do vetor: ',media)