'''Faça um algoritmo que leia o nome e a idade de uma pessoas, verique se a idade de uma pessoa é menor ou maior de idade. Considera-se maior de idade uma pessoa com 18 anos ou mais. Como saída o algoritmo deve informar o nome e a idade da pessoa e depois uma mensagem se ela é ou não maior de idade'''

nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
if idade >= 18:
    print('Nome: ',nome)
    print('Idade: ',idade)
    print('Maior de idade')
else:
    print('Nome: ',nome)
    print('Idade: ',idade)
    print('Menor de idade')
