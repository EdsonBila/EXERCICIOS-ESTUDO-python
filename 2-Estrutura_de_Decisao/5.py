'''Elabore um algoritmo que informando a idade de um nadador o mesmo terá condições de classicar em uma das seguintes categorias: infantil = 5 - 10 anos; juvenil = 11-17 anos; adulto = maiores de 18 anos.'''

idade = int(input('Informe sua idade: '))
if idade >=5 and idade <=10:
    print('Tem condições de se classificar na categoria: infantil')

elif idade >=11 and idade <=17:
    print('Tem condições de se classificar na categoria: juvenil')

elif idade <5:
    print('Nao tem condições de classificar em nenhuma categoria')

else:
    print('Tem condições de se classificar na categoria: adulto')
