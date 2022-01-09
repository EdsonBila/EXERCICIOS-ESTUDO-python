'''Faça um programa que carregue um vetor com nota de dez alunos, calcule
e mostre a MÉDIA DA SALA e quantos alunos estão acima e abaixo da média
da sala.'''

nota = []
soma = 0
mediaClasse = 0
for i in range(4):
    nota.append(float(input('Informe a nota: ')))
    soma = soma + nota[i]
mediaClasse = soma/len(nota)

alunosacima = 0
alunosabaixo = 0
for o in range(4):
    if nota[o] >= mediaClasse:
        alunosacima = alunosacima + 1
    if nota[o] < mediaClasse:
        alunosabaixo = alunosabaixo + 1
print('A media da classe é de',mediaClasse)
print('Quantidade de alunos acima da média: ',alunosacima)
print('Quantidade de alunos abaixo da média: ',alunosabaixo)