''' Faça um programa que receba três números obrigatoriamente em ordem crescente e um quarto número que não siga essa regra. Mostre, em seguida, os quatro números em ordem decrescente. Suponha que o usuário digitará quatro números diferentes.'''

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número maior: '))
if n1 < n2:
    n3 = float(input('Digite um número maior ainda: '))
    if n2 < n3:
        n4 = float(input('Digite outro número: '))
        if n4 == n1 or n4 == n2 or n4 == n3:
            print('Tem que ser diferente de: ',n1,'-',n2,'e',n3)
        elif n4 > n3:
            print('A ordem decrescente é: ',n4,'-',n3,'-',n2,'-',n1)
        elif n4 > n2 and n4 < n3:
            print('A ordem decrescente é: ',n3,'-',n4,'-',n2,'-',n1)
        elif n4 > n1 and n4 < n2:
            print('A ordem decrescente é: ',n3,'-',n2,'-',n4,'-',n1)
        elif n4 < n1:
            print('A ordem decrescente é: ',n3,'-',n2,'-',n1,'-',n4)
    else:
        print('Tem que ser maior')
else:
    print('Tem que ser maior')
