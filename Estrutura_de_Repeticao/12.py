'''Construir um algoritmo que, dado o valor de 20 preços de TV, determine
e apresente o valor mais caro e mais barato entre eles.'''

barato = 10000
caro = 0
contador = 0
while contador < 4:
    valorTv = float(input('Informe o valor da TV: '))
    if valorTv >= caro:
        caro = valorTv
    if valorTv < barato:
        barato = valorTv
    contador+=1
print('Esse é o valor de TV mais caro: ',caro)
print('Esse é o valor de TV mais barato: ',barato)