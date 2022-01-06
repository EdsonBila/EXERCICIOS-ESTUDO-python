'''Faça um programa que receba a altura e peso de uma pessoa. De acordo
com a tabela a seguir, verique e mostre a classicação dessa pessoa.
ALTURA           | ATÉ 60 | ENTRE 60 E 90 (INCLUSIVE) | ACIMA DE 90
Menores que 1,20 | A      | D                         | G
De 1,20 a 1,70   | B      | E                         | H
Maiores que 1,70 | C      | F                         | I'''

a = float(input('digite a sua altura: '))
p = float(input('digite o seu peso Kg: '))
if a < 1.20:
    if p <= 60:
        print('classificação: A')
    elif 60 < p <= 90:
        print('classificação: D')
    else:
        print('classificação: G')
elif 1.20 <= a <= 1.70:
    if p <= 60:
        print('classificação: B')
    elif 60 < p <= 90:
        print('classificação: E')
    else:
        print('classificação: H')
else:
    if p <= 60:
        print('classificação: C')
    elif 60 < p <= 90:
        print('classificação: F')
    else:
        print('classificação: I')