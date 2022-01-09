'''Faça um programa que:
    Preencha um vetor com sete números inteiros,
Calcule (%) e mostre os números:
    Múltiplos de 2;
    Múltiplos de 3;
    Múltiplos de 2 e de 3.'''

n = []
nm2 = []
nm3 = []
for i in range(7):
    n.append(int(input('Informe um número inteiro: ')))
    mult2 = 2 * n[i]
    mult3 = 3 * n[i]
    if mult2 == n[i]:
        nm2.append(n[i])
    if mult3 == n[i]:
        nm3.append(n[i])
    if mult2 != n[i] or mult3 != n[i]:
        print('hhh')
print('Os números múltiplos de 2 são:',nm2)
print('Os números múltiplos de 3 são:',nm3)