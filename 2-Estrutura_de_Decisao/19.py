'''Faça um programa que apresente o menu a seguir, permita ao usuário
escolher a opção desejada, receba os dados necessários para executar a
operação e mostre o resultado. Verique a possibilidade de opção inválida e
não se preocupe com restrições, como salário negativo.

Menu de opções
1. Imposto
2. Novo salário
3. Classificação
Digite a opção desejada:

Na opção 1: receber o salário de um funcionário, calcular e mostrar o valor do imposto usando as
regras a seguir.
SALÁRIO                                    | PERCENTUAL DO IMPOSTO
Menor que 500,00                           | 5%
De 500,00 (inclusive) a 850,00 (inclusive) | 10%
Acima de 850,00                            | 15%

Na opção 2: receber o salário de um funcionário, calcular e mostrar o valor do novo salário,
usando as regras a seguir.
SALÁRIO                                      | AUMENTO
Maior que 1.500,00                           | 25,00
De 750,00 (inclusive) a 1.500,00 (inclusive) | 50,00
De 450,00 (inclusive) a 750,00               | 75,00
Menor que 450,00                             | 100,00

Na opção 3: receber o salário de um funcionário e mostrar sua classicação usando a tabela a
seguir.
SALÁRIO                | CLASSIFICAÇÃO
Até 700,00 (inclusive) | Mal remunerado
Maiores que 700,00     | Bem remunerado'''

print('menu de opções')
print('1. Imposto')
print('2. Novo salário')
print('3. Classificação')
o = int(input('Digite a opção desejada: '))
if o == 1:
    s = float(input('digite o salário do funcionário R$: '))
    if s < 500.00:
        i = s * 5 / 100
    elif 500.00 <= s <= 850.00:
        i = s * 10 / 100
    else:
        i = s * 15 / 100
    print('O imposto a ser aplicado é de R$: ',i)
elif o == 2:
    s = float(input('digite o salário do funcionário R$: '))
    if s > 1500.00:
        s_a = s + 25.00
    elif 750.00 <= s <= 1500.00:
        s_a = s + 50.00
    elif 450.00 <= s <= 750.00:
        s_a = s + 75.00
    else:
        s_a = s + 100.00
        print('total do salário com aumento R$: ',s_a)
elif o == 3:
    s = float(input('digite o salário do funcionário R$: '))
    if s <= 700.00:
        print('Mal remunerado')
    else:
        print('Bem remunerado')
else:
 print('Dado inválido, digite uma opção válida')