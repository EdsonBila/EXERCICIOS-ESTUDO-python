'''Faça um algoritmo que calcule e apresente a média de idades de uma
sala de 35 alunos.'''

soma = 0
idade = []
for i in range(8):
    idade.append(int(input('Informe a idade: ')))
    soma = soma + idade[i]
media = soma/8
print('A média de idade é',media)