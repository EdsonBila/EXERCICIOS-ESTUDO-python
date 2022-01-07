'''Faça um algoritmo que leia de dez alunos altura e nome. Mostre o aluno
mais alto e mais baixo e seus respectivos nomes.'''

alto = 0
nomeAlto = ''
baixo = 2
nomeBaixo = ''
contador = 0
while contador < 3:
    nome = input('Informe o nome: ')
    altura = float(input('Informe a altura: '))
    if altura >= alto:
        alto = altura
        nomeAlto = nome
    if altura < baixo:
        baixo = altura
        nomeBaixo = nome
    contador+=1
print(nomeAlto,'é mais alto, com uma altura de',alto)
print(nomeBaixo,'é mais baixo, com uma altura de',baixo)