'''Faça um programa que:
    Preencha dois vetores com de dez numeros cada
    Preecha um terceira vetor com os números dos dois vetores anteriores ordenados em
    ordem crescente'''

v1 = [1,4,5,8,7,2,5,8,4,6]
v2 =[15,14,18,58,69,25,57,43,71,327,48]
v3 = []

v3 = v1+v2
v3.sort()
print('lista em ordem crescente: ',v3)