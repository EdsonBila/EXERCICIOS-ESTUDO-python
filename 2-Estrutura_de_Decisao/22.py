''' Um supermercado deseja reajustar os preços de seus produtos usando o
seguinte critério: o produto poderá ter seu preço aumentado ou diminuído.
Para o preço ser alterado, o produto deve preencher pelo menos um dos
requisitos a seguir:
VENDA MÉDIA MENSAL | PREÇO ATUAL        | % DE AUMENTO | % DE DIMINUIÇÃO
< 500              | < 30.000           | 10           | -
>= 500 e <1.200    | >= 30,00 e < 80,00 | 15           | -
>= 1,200           | >= 80,00           | -            | 20

aça um programa que receba o preço atual e a venda média mensal do produto, calcule e
mostre o novo preço.'''

p_a = float(input('digite o preço atual do produto R$: '))
m_m_v = int(input('digite a média mensal de vendas R$: '))
if m_m_v < 500 or p_a < 30:
    n_p = p_a + 10 / 100 * p_a
elif 500 <= m_m_v < 1200 or 30 <= p_a < 80:
    n_p = p_a + 15 / 100 * p_a
elif m_m_v >= 1200 or p_a >= 80:
    n_p = p_a - 20 / 100 * p_a
print('novo preço R$: ',n_p)