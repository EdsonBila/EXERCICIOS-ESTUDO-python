'''A Organização Mundial de Saúde usa a seguinte tabela para determinar a
condição de um adulto, para isso desenvolva um algoritmo para calcular o
Índice de Massa Corporal (IMC) e apresenta-lo, dado pela fórmula:
 IMC = peso / (altura)2 (o 2 elevado ao quadrado)
CONDIÇÃO       | IMC em adultos
Abaixo do peso | Abaixo de 18.5
No peso normal | Entre 18.5 e 25
Acima do peso  | Entre 25.1 e 30
Obeso          | Acima de 30'''

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = round(peso / altura ** 2)
if imc <= 18.5:
    print('Abaixo do peso: ',imc)
elif imc > 18.5 and imc <=25:
    print('No peso normal: ',imc)
elif imc >= 25.1 and imc <=30:
    print('Acima do peso: ',imc)
else:
    print('Obeso: ',imc)
