'''Faça um programa que receba:
o código do estado de origem da carga de um caminhão, supondo que a digitação do
código do estado seja sempre válida, isto é, um número inteiro entre 1 e 5;
o peso da carga do caminhão em toneladas;
o código da carga, supondo que a digitação do código seja sempre válida, isto é, um
número inteiro entre 10 e 40.
CÓDIGO DO ESTADO | IMPOSTO
1                | 35%
2                | 25%
3                | 15%
4                | 5%
5                | Isento

CÓDIGO DO ESTADO | IMPOSTO
2                | 25%
3                | 15%
4                | 5%
5                | Isento

Calcule e mostre:
o peso da carga do caminhão convertido em quilos;
o preço da carga do caminhão;
o valor do imposto, sabendo que o imposto é cobrado sobre o preço da carga do
caminhão e depende do estado de origem;
o valor total transportado pelo caminhão, preço da carga mais imposto.'''

codigo_do_estado = int(input('Código do estado: '))
peso_em_toneladas = float(input('Peso de carga em toneladas: '))
codigo_da_carga = int(input('Código da carga: '))
peso_em_quilos = peso_em_toneladas * 1000
print('Peso em quilos: ',peso_em_quilos)
if codigo_da_carga >= 10 and codigo_da_carga <= 20:
    preco_da_carga = 100 * peso_em_quilos
elif codigo_da_carga >= 21 and codigo_da_carga <= 30:
    preco_da_carga = 250 * peso_em_quilos
elif codigo_da_carga >= 31 and codigo_da_carga <= 40:
    preco_da_carga = 340 * peso_em_quilos
print('Preço de carga: ',preco_da_carga)
if codigo_do_estado == 1:
    imposto = 35/100 * preco_da_carga
elif codigo_do_estado == 2:
    imposto = 25/100 * preco_da_carga
elif codigo_do_estado == 3:
    imposto = 15/100 * preco_da_carga
elif codigo_do_estado == 4:
    imposto = 5/100 * preco_da_carga
elif codigo_do_estado == 5:
    imposto = 0
print('Imposto: ',imposto)
valor_total = preco_da_carga + imposto
print('Valor total', valor_total)