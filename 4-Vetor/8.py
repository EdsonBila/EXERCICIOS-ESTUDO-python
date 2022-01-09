'''Criar um algoritmo que a partir de um vetor de 10 elementos inteiros, crie
outros dois vetores, um deles armazenará os elementos positivos e o outro
os negativos e ao nal apresente-os.'''

Ninteiros = []
Npositivos = []
Nnegativos = []
for i in range(5):
    Ninteiros.append(int(input('Informe um número inteiro: ')))
for o in range(5):
    if Ninteiros[o] >= 0:
        Npositivos.append(Ninteiros[o])
    if Ninteiros[o] < 0:
        Nnegativos.append(Ninteiros[o])
print('Os números positivos são: ',Npositivos)
print('Os números negativos são: ',Nnegativos)