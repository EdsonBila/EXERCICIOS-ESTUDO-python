'''Foi feita uma pesquisa com as crianças de uma determinada localidade.
Faça um programa que: 
    Superiorleia o número de crianças nascidas no período;
    identique o sexo (M ou F) e a idade da criança.
O programa deve calcular e mostrar:
    a percentagem de crianças do sexo marculino;
    a percentagem de crianças do sexo feminino;
    a percentagem de crianças menores que 24 meses.'''

total_de_meninos = 0
total_de_meninas = 0
criancas_menores_de_24_mese = 0
total_de_criancas_nascidas = int(input('Informe o total de crianças: '))
for contador in range(total_de_criancas_nascidas):
    sexo = input('Informe o sexo (M ou F) da criança: ')
    idade = int(input('Informe a idade(em anos) da criança: '))
    if sexo == 'M' or sexo == 'm':
        total_de_meninos = total_de_meninos + 1
        porcentagem_de_meninos = (total_de_meninos / (total_de_criancas_nascidas * 100))
    elif sexo == 'F' or sexo == 'f':
        total_de_meninas = total_de_meninas + 1
        porcentagem_de_meninas = (total_de_meninas / (total_de_criancas_nascidas * 100))
    if idade < 2:
        criancas_menores_de_24_mese = idade
        porcentagem_de_criancas_menores_de_24_mese = criancas_menores_de_24_mese / total_de_criancas_nascidas*100
print('A porcentagem de crianças do sexo Masculino é de',porcentagem_de_meninos,'%')        
print('A porcentagem de crianças do sexo Feminino é de',porcentagem_de_meninas,'%')
print('A porcentagem de crianças menores de 2 anos é de',porcentagem_de_criancas_menores_de_24_mese,'$')