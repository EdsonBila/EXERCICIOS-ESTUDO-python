'''Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento de um mês.'''
deposito = float(input('Digite o valor do Depósito: '))
taxa = float(input('Digite o valor da taxa de juros: '))
rendimento = deposito * taxa / 100
total = deposito + rendimento
print('Rendimento: ',rendimento)
print('Total a ser recebido após um mês de rendimento: ',total)