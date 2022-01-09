'''Escreva um algoritmo que receba 23 números, calcule e exiba a
quantidade de números pares e impares.'''

qpares = 0
qimpares = 0
contador = 1
while contador <= 23:
  numeroR = float(input('Informe um valor: '))
  if numeroR%2 == 0:
    qpares = qpares + 1
  else:
    qimpares = qimpares + 1
  contador+=1
print('Números par: ',qpares)
print('Número impar: ',qimpares)