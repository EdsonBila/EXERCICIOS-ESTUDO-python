'''Faça um programa que mostre o menu de opções a seguir, receba a
opção do usuário e os dados necessários para executar cada operação.
Menu de opções:
1. Somar dois números.
1. Raiz quadrada de um número.
Digite a opção desejada:'''

print('Menu de opções: ')
print('1-Somar dois números')
print('2-Raiz quadrada de um número')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
 n1 = float(input('Digite qualquer número: '))
 n2 = float(input('Digite qualquer numero: '))
 resultado = n1 + n2
 print('A soma dos dois números é: ',resultado)
elif opcao == 2:
 n = float(input('Digite qualquer número: '))
 raiz1 =( n **(1/2))
 raiz2 = round(n ** (1/2))
 print('A raiz quadrada do numero é: ',raiz1)
 print('Arredondado: ',raiz2)