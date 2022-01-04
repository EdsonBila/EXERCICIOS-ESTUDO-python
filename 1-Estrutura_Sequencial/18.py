'''Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os quais fornece a quantidade de ração em gramas. A quantidade diária de ração fornecida para cada gato é sempre a mesma. Faça um programa que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato, calcule e mostre quanto restará de ração no saco após cinco dias.'''
peso_saco = float(input('Peso do saco de ração: '))
racao_gato1 = float(input('Quantidade de ração: '))
racao_gato2 = float(input('Quantidade de ração: '))
Racao_gato1 = racao_gato1 / 1000
Racao_gato2 = racao_gato2 / 1000
total_final = peso_saco - 5 * (Racao_gato1 + Racao_gato2)
print('Restante total de ração: ',total_final)