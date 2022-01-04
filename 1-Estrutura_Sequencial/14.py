'''Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: a idade dessa pessoa; quantos anos ela terá em 2050.'''
ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade_atual = ano_atual - ano_nascimento
idade_2050 = 2050 - ano_nascimento
print('Sua idade atual: ',idade_atual)
print('Sua idade em 2050: ',idade_2050)

