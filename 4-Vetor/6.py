''' Faça um programa que carregue um vetor com dez nomes e faça uma
vericação se um determinado nome esta nesse vetor. Se não conter o
nome pesquisado informe que não encontrou. A frase "Não encontrou",
quando for o caso deverá ser apresentada APENAS UMA VEZ'''

nomes = []
pesquisa = []
for i in range(4):
    nomes.append(input('Registre um nome: '))
print('<=>'*20)
pesquisa.append(input('Insira um nome para verificação: '))
for o in range(1):
    if pesquisa[o] == nomes[o]:
        print('NOME ENCONTRADO: ',pesquisa[o])
    else:
        ('NÃO ENCONTROU')
