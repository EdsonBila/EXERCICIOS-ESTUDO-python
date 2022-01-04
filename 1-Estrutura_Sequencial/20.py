'''Faça um programa que receba a medida do ângulo (em graus) formado por uma escada apoiada no chão e encostada na parede e a altura da parede onde está a ponta da escada. Calcule e mostre a medida dessa escada. Observação: as funções trigonométricas implementadas nas linguagens de programação trabalham com medidas de ângulos em radianos.'''
import math
angulo = int(input('Informe um angulo: '))
altura = float(input('Informe uma altura: '))
radiano = angulo * 3.14 / 180
escada = altura / math.sin(radiano)
print('Medida da escada: ',escada)