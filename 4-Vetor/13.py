'''Faça um programa que:
    Preencha um vetor com quinze elementos inteiros
    Verique a existência de elementos iguais a 30, mostrando as posições em que
    apareceram.'''
    
n = [1,2,30,4,5,5,3,30,7,8,30]
if 30 in n:
    print('O elemento é igual a 30 e tem como posição:',n.index(30))

'''
n = []
for i in range(15):
    n.append(int(input('Informe um número inteiro: ')))
    if n[i] == 30:
        print('O elemento é igual a 30 e tem como posição:',i)
'''