'''Faça um programa que:
    leia um valor N inteiro e positivo'''

contador = 1

fatorial = 1
calculo = 1
n = int(input('Informe um número inteiro e positivo: '))
for contador in range(n+1):
    while calculo <= n:
      fatorial *= calculo
      calculo += 1
    E = calculo/fatorial + 1
print('{}! = {}'.format(n,fatorial))