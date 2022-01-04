'''Cada degrau de uma escada tem X de altura. Faça um programa que receba essa altura e a altura que o usuário deseja alcançar subindo a escada, calcule e mostre quantos degraus ele deverá subir para atingir seu objetivo, sem se preocupar com a altura do usuário. Todas as medidas fornecidas devem estar em metros.'''
altura_do_degrau = float(input('Digite a altura do degrau: '))
altura_desejada = float(input('Digite a altura desejada: '))
quantidade_de_degraus = altura_desejada // altura_do_degrau
print('Quantidade de degraus: ',quantidade_de_degraus)

