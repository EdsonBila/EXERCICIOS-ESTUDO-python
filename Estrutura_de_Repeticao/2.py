'''Faça um algoritmo que mostre o cumprimento ‘Olá ‘ para o nome de
alguém (4 pessoas). Exemplo ‘Olá Mariana’.'''

print('NOMES')
contador = 1
while contador <= 4:
    nome = input('Qual seria o seu nome? ')
    print('Olá!', nome)
    contador+= 1
