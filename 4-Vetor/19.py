''''Faça um programa que:
    Preencha dois vetores com 10 números cada
    Faça a multiplicação dos números na mesma posição V1[0] * V2[0] ...
    O resultado deverá ser inserido no terceiro vetor'''

v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v3 = []
for i in range(10):
    v3.append(v1[i] * v2[i])
print('resultado da multiplicação',v3)