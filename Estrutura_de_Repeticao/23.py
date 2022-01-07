'''Elabore um algoritmo que informada a idade de 10 nadadores o mesmo
terá condições de classicar em uma das seguintes categorias: infantil = 5 -
10 anos; juvenil = 11-17 anos; adulto >= maiores de 18 anos. USE DUAS
ESTRUTURAS DE REPETIÇÃO'''

contador = 1
while contador <= 10:
    
    idade = int(input('Informe sua idade: '))
    if idade < 5:
        print('Sem classificação')
    elif idade <= 10:
        print('Você tem condições de classificar na categoria INFANTIL')
    elif idade <= 17:
        print('Você tem condições de classificar na categoria JUVENIL')
    else:
        print('Você tem condições de classificar na categoria ADULTO')
    contador +=1