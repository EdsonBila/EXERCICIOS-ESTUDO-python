'''Elabore um algoritmo que calcule e informe a média de idades de 5
alunos.'''

acumulaidade = 0
contador = 0
while contador < 5:
    idade = int(input('Informe a sua idade: '))
    acumulaidade = acumulaidade + idade
    contador +=1
media = acumulaidade/contador
print('A média das idades dos alunos são: ',media)