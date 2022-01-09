'''Construir um algoritmo para calcular a média aritmética de preços de 5
produtos.'''

acumulapreco = 0
contador = 0
while contador < 5:
    precos = float(input('Informe o preço do produto: '))
    acumulapreco = acumulapreco + precos
    contador +=1
media = acumulapreco/contador
print('A média dos preços dos produtos são: ',media)