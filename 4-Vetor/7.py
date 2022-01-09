'''Faça um algoritmo que calcule e apresente a média de alturas superior a
1.80. Informe também quantos e quais (posição) são os alunos.'''

soma_altura_alunos = 0
altura_alunos = []
quantidade_alunos = 0
qalunos = int(input('Quantidade de alunos: '))
for i in range(qalunos):
    altura_alunos.append(float(input('Informe a altura: ')))
    if altura_alunos[i] > 1.8:
        soma_altura_alunos += altura_alunos[i]
        quantidade_alunos += 1
media = soma_altura_alunos /quantidade_alunos
print('A média de altura superior a 1.80 é: ',media)
print('Número de alunos com altura superior a 1.80: ',quantidade_alunos)
for o in range(qalunos):
    if altura_alunos[o] > 1.8:
        print('O aluno número',o,'possui',altura_alunos[o],'de altura')