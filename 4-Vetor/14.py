'''Faça um programa que:
    Preencha um vetor com dez números reais (oat)
Calcule e mostre:
    A quantidade de números negativos
    A soma dos números positivos desse vetor. Não use a função sum().'''
    
n = []
npositivos = []
somapositivos = 0
nnegativos = []
contnegativos = 0
for i in range(10):
    n.append(float(input('Informe um número: ')))
    if n[i] >= 0:
        npositivos.append(n[i])
        somapositivos += n[i]
    if n[i] < 0:
        nnegativos.append(n[i])
        contnegativos += 1
print('A quantidade de números negativos é de:',contnegativos)
print('A soma dos números positivos é de:',somapositivos)