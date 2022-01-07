'''Faça um algoritmo que conheça 4 valores diferentes, some-os e mostre o
resultado.'''

acumulaValor = 0 
contador = 0
while contador < 4:
    numero = float(input('Informe um valor numérico: '))
    acumulaValor = acumulaValor + numero 
    contador +=1
print('Valor total dos valores somados: ',acumulaValor)