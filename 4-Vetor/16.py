'''Faça um programa que:
    Receba cinco números e mostre a saída a seguir:
    Imprima a seguinte saída: n1 + n2 + n3 + n4 + n5 = soma_dos_numeros(valor)'''

n = []
soma = 0
for i in range(5):
    n.append(int(input('Informe um número: ')))
    soma += n[i]
print('A soma dos numeros é',soma)