'''Faça um programa que carregue um vetor de dez elementos que contenha
o nome de pessoas e outro que contenha o peso, encontre qual a pessoa
mais gorda e mais magra e apresente o nome e o peso das mesmas. Não
utilize as funções: min(), max()'''

nome = []
peso = []
mgordo = 0
mmagro = 400
nmgordo = ''
nmmagro = ''
for i in range(5):
    nome.append(input('Informe o nome: '))
    peso.append(float(input('Informe o peso: ')))
    if peso[i] >= mgordo:
        mgordo = peso[i]
        nmgordo = nome[i]
    if peso[i] < mmagro:
        mmagro = peso[i]
        nmmagro = nome[i]
print('A pessoa com nome',nmgordo,' é o(a) com mais peso, com um peso de',mgordo)
print('A pessoa com nome',nmmagro,' é o(a) com menos peso, com um peso de',mmagro)