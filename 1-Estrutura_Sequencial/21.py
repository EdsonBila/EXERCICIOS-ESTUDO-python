'''Uma pessoa deseja pregar um quadro em uma parede. Faça um programa para calcular e mostrar a que distância a escada deve estar da parede. A pessoa deve fornecer o tamanho da escada e a altura em que deseja pregar o quadro. Lembre-se de que o tamanho da escada deve ser maior que a altura que se deseja alcançar.'''
z = float(input('Digite o tamanho da escada: '))
x = float(input('Digite a altura em que deseja pregar o quadro: '))
y = (z ** 2) - (x ** 2)
h = y ** (1/2)
print('Distância entre a parede e a escada = ',h)
