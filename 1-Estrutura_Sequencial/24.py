'''Faça um programa que receba uma hora formada por hora e minutos (um número real), calcule e mostre a hora digitada apenas em minutos'''
hora = float(input('Informe a hora: '))
h = int(hora)
minutos = hora - h
conversao = (h * 60) + (minutos * 100)
print('Conversão: ',conversao)
