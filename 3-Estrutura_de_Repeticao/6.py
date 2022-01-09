'''Faça um algoritmo que receba a idade de 10 pessoas, calcule e exiba a
quantidade de pessoas maiores de idade, sendo que a maioridade é obtida
após completar 18 anos.'''

idade = 0
for contador in range(10):
    i = int(input('Informe a sua idade: '))
    if i >= 18:
        idade += 1
print('Quantidade de pessoas maior de idade: ',idade)

print('COM WHILE <=>'*15)

contador = 1
qPessoas = 0
while contador <= 10:
    idade = int(input('informe a sua idade: '))
    if idade >= 18:
        qPessoas = qPessoas + 1
    contador = contador + 1
print('Qde pessoas',qPessoas)
