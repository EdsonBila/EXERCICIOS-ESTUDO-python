'''Faça um programa para calcular a tabuada do 2 até a do 9. USE DUAS
ESTRUTURAS DE REPETIÇÃO'''

for tabuada in range(2,10):
    for n in range(1,11):
        print(tabuada,'x',n,'=',tabuada * n)
    print('<=>'*15)