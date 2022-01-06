''' Faça um programa que receba o valor do salário mínimo, o número de
horas trabalhadas, o número de dependentes do funcionário e a quantidade
de horas extras trabalhadas. Calcule e mostre o salário a receber do
funcionário de acordo com as regras a seguir:
O valor da hora trabalhada é igual a 1/5 do salário mínimo;
O salário do mês é igual ao número de horas trabalhadas multiplicado pelo valor da hora
trabalhada;
Para cada dependente, acrescentar 32,00;
Para cada hora extra trabalhada, calcular o valor da hora * trabalhada acrescida de 50%;
O salário bruto é igual ao salário do mês mais o valor dos dependentes mais o valor das
horas extras;
Calcular o valor do impostoosto de renda retido na fonte de acordo com a tabela a seguir:
IRFF   | SALÁRIO BRUTO
Isento | Inferior a 200,00
10%    | De 200,00 até 500,00
20%    | Superior a 500,00

O salário líquido é igual ao salário bruto menos IRRF.
A graticação é de acordo com a tabela a seguir:
SALÁRIO LÍQUIDO | GRATIFICAÇÃO
Até 350,00      | 100,00
Superior a 350  | 50,00

O salário a receber do funcionário é igual ao salário líquido mais a graticação.'''

s_m = float(input('digite o valor do salário mínimo R$: '))
h_t = float(input('digite o número de horas trabalhadas: '))
h_e = float(input('digite o número de horas extras trabalhadas: '))
n_d = int(input('digite o número de dependentes: '))
vht = s_m / 5
sdm = h_t * vht
ad = n_d * 32
vhe = vht + (vht * 50 / 100)
she = h_e * vhe
sb = sdm + ad + she
if sb < 200:
    irff = 0
elif 200 <= sb <= 500:
    irff = sb * 10 / 100
else:
    irff = sb * 20 / 100
sl = sb - irff
if sl <= 350:
    g = 100
else:
    g = 50
s_a_r = sl + g
print('salário á receber R$: ',s_a_r)