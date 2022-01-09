'''Um vetor é palíndromo se ele não se alterar quando o mesmo for
invertido. Por exemplo, o vetor original vo = {1, 3, 5, 2, 2, 5, 3, 1} é palíndromo,
pois ele invertido é vi = {1, 3, 5, 2, 2, 5, 3, 1}, igual ao original. Escreva um
algoritmo que verique se um vetor é palíndromo, fazendo comparação de
posição por posição do vetor origem (vo) com o vetor invertido(vi). Não pode
usar a função reverse().'''

Voriginal = []
for i in range(5):
    Voriginal.append(int(input(f'Informe o {i + 1}º número: ')))
print(Voriginal)
Vinvertido = []
for i in range(4,-1,-1):
    Vinvertido.append(Voriginal[i])
print(Vinvertido)
cont = 0
for i in range(5):
    if Voriginal[i] == Vinvertido[i]:
        cont = cont + 1
if cont == len(Voriginal):
    print('É palíndromo')
else:
    print('Nâo é palíndromo')