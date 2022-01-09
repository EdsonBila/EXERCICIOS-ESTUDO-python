''''Faça um programa que:
    Leia um vetor com 10 números inteiros
    Exiba apenas os números positivos.'''

n = [-1, 2, 3, -4, 5, -6, 7, 8, 9, -10]
n_p = []
for i in range(len(n)):
    if n[i] >=0:
        n_p.append(n[i])
print(n_p)
