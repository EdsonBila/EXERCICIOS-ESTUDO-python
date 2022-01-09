'''Faça um algoritmo que calcule e apresente a média de alturas (vetor) de
uma sala de 35 alunos. Informe também quantos alunos e quais (posição)
são os que possuem idade (outro vetor) superior a 25 anos. '''

soma = 0
altura = []
idade = []
for i in range(4):
    altura.append(float(input('Informe a altura: ')))
    idade.append(int(input('Informe a idade: ')))
    soma = soma + altura[i]
media = soma/len(altura)
print('______________________')
print('A média de altura é',media)
print('______________________')
contador = 0
for o in range(4):
    if idade[o] > 25:
        contador = contador + 1
        print('Aluno de Nº',o,' tem idade superior a 25, com idade de',idade[o])
print('A quantidade de alunos com idade maior de 25 anos é',contador)