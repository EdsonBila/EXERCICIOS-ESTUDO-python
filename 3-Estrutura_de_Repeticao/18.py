'''Faça um programa que receba duas notas de seis alunos. Calcule e
mostre:
    a média aritmética das duas notas de cada aluno; e
    a mensagem que está na tabela a seguir:
        Média aritimética | Mesagem
        Até 3             | Reprovado
        Entre 3 e 7       | Exame
        De 7 para cima    | Aprovado
o total de alunos aprovados;
o total de alunos de exame;
o total de alunos reprovados;
a média da classe'''

somaMedia = 0
totalReprovado = 0
totalExame = 0
totalAprovados = 0
for contador in range(6):
    nota1 = float(input('Informe a 1 nota: '))
    nota2 = float(input('Informa a 2 nota: ')) 
    mediaA = (nota1 + nota2)/ 2
    somaMedia = somaMedia + nota1
    somaMedia = somaMedia + nota2
    mediaClasse = somaMedia/12
    if mediaA <= 3:
        totalReprovado = totalReprovado + 1
        print('A sua Média é de',mediaA,', então você está Reprovado')
    elif mediaA > 3 and mediaA < 7:
        totalExame = totalExame + 1
        print('A sua Média é de',mediaA,', então você está em Exame')
    elif mediaA >= 7:
        totalAprovados = totalAprovados + 1
        print('A sua Média é de',mediaA,', então você está Aprovado')
    print('_'*21)
print('O total de alunos reprovados são: ',totalReprovado)
print('O total de alunos de exame são: ',totalExame)
print('O total de alunos aprovados são: ',totalAprovados)

print('A media da classe é de',mediaClasse)