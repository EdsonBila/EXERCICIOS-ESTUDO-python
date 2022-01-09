'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados
sobre acidentes de trânsito. Foram obtidos os seguintes dados:
    nome da cidade;
    número de veículos de passeio;
    número de acidentes de trânsito com vítimas.
Deseja-se saber:
    o maior índice de acidentes de trânsito e a que cidades pertence;
    o menor índice de acidentes de trânsito e a que cidades pertence;
    qual é a média de veículos nas cinco cidades juntas;
    qual é a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de
    passeio.'''
    
total_cidades_pesquisadas = 5
somatoria_veiculos_nas_cidades = 0
somatoria_acidentes_cidades_com_mais_2000_veiculos = 0
numero_cidades_mais_200_veiculos = 0

for contador in range(total_cidades_pesquisadas):
     nome_cidade = input('Informe o nome da cidade: ')
     numero_veiculos = int(input('Informe o número de veículos: '))
     numero_acidentes = int(input('Informe o número de acidentes de tránsito: '))
     if contador == 0:
        maior_indice_acidentes = numero_acidentes
        cidade_maior_indice_acidentes = nome_cidade
        menor_indice_acidentes = numero_acidentes
        cidade_menor_indice_acidentes = nome_cidade
     else:
        if numero_acidentes > maior_indice_acidentes:
          maior_indice_acidentes = numero_acidentes
          cidade_maior_indice_acidentes = nome_cidade
        if numero_acidentes < menor_indice_acidentes:
          menor_indice_acidentes = numero_acidentes
          cidade_menor_indice_acidentes = nome_cidade
     somatoria_veiculos_nas_cidades += numero_veiculos
     
     if numero_veiculos > 2000:
         somatoria_acidentes_cidades_com_mais_2000_veiculos += numero_acidentes
         numero_cidades_mais_200_veiculos += 1
media_carros_cidades = (somatoria_veiculos_nas_cidades/total_cidades_pesquisadas)
 
if numero_cidades_mais_200_veiculos == 0:
    print('Não foi informada nenhuma cidade com menos de 2000 veículos')
else:
    media_acidentes_cidade_mais_2000_veiculos = (somatoria_acidentes_cidades_com_mais_2000_veiculos/numero_cidades_mais_200_veiculos)
    print('A',cidade_maior_indice_acidentes,'tem um total de',maior_indice_acidentes,'acidentes de tránsito')
    print('A',cidade_menor_indice_acidentes,'é a que tem os menores casos de acidentes, com um total de',menor_indice_acidentes) 
    print('Média de veículos nas cinco cidades juntas: ',media_carros_cidades)
    print('A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é de',media_acidentes_cidade_mais_2000_veiculos)