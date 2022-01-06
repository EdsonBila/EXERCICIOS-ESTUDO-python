'''Tendo como dados de entrada a altura e o sexo (M/F) de uma pessoa (Mmasculino ou F-feminino), construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: homem: (72.7 * altura) - 58; mulher: (62.1 * altura) - 44.7;'''

sexo = input('Informe o sexo: ')
altura = float(input('Informe a altura: '))
if sexo == 'Masculino' or sexo == 'masculino':
    M = round(72.7 * altura) - 58
    print('Seu peso ideal: ',M)
elif sexo == 'Feminino' or sexo == 'feminino':
    F = round(62.1 * altura) - 44.7
    print('Seu peso ideal: ',F)
