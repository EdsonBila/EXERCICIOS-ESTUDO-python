'''Sabe-se que: pé = 12 polegadas, 1 jarda = 3 pés, 1 milha = 1,760 jarda. Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.'''
pes = float(input('Digite um valor em pés: '))
polegadas = pes * 12
jardas = pes / 3
milhas = jardas / 1760
print('Polegadas: ',polegadas)
print('Jardas: ',jardas)
print('Milhas: ',milhas)

