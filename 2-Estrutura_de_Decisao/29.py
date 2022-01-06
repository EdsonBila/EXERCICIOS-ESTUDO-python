'''Faça um programa que:
     receba o valor do salário mínimo,
    o turno de trabalho (M — matutino; V — vespertino; ou N — noturno),
    a categoria (O — operário; G — gerente)
    número de horas trabalhadas no mês de um funcionário.
Suponha a digitação apenas de dados válidos e, quando houver digitação de letras, utilize
maiúsculas.

Calcule e mostre:
    O coeciente do salário, de acordo com a tabela a seguir.
        TURNO DE TRABALHO | VALOR DO COEFICIENTE
        M - Matutino | 10% do salário mínimo
        V - Vespertino | 15% do salário mínimo
        N - Noturno | 20% do salário mínimo

    O valor do salário bruto, ou seja, o número de horas trabalhadas multiplicado pelo valor do
    coeciente do salário.

    O imposto, de acordo com a tabela a seguir.
        CATEGORIA    | SALÁRIO BRUTO | IMPOSTO SOBRE O SALÁRIO BRUTO
        O - Operário | >= 300,00     | 5%
        O - Operário | < 300,00      | 3%
        G - Gerente  | >= 300,00     | 6%
        G - Gerente  | < 300,00      | 4%
    A graticação, de acordo com as regras a seguir. Se o funcionário preencher todos os
    requisitos a seguir, sua graticação será de 50,00; caso contrário, será de 30,00. Os
    requisitos são:
        Turno: Noturno
        Número de horas trabalhadas: Superior a 80 horas
        O auxílio alimentação, de acordo com as seguintes regras
        
    Auxilio alimentação, um terço do seu salário bruto; caso contrário, será de metade do seu
    salário bruto. Os requisitos são:
        Se o funcionário preencher algum dos requisitos a seguir, seu auxílio alimentação
        será de
        Categoria: Operário
        Coeciente do salário: < = 25
    O salário líquido, ou seja, salário bruto menos imposto mais graticação mais auxílio
    alimentação.
    
    A classicação, de acordo com a tabela a seguir:
        SALÁRIO LÍQUIDO    | MENSAGEM
        Menor que 350,00   | Mal remunerado
        Entre 350 e 600,00 | Normal
        Maior que 600,00   | Bem remunerado'''

sal_min = float(input('Informe o seu salário minimo: '))
print('TURNOS:')
print('M - matutino')
print('V - vespertino')
print('N - noturno')
turno = input('Informe o turno: ')
print('CATEGORIAS:')
print('O - operário')
print('G - gerente')
categ = input('Informe a categoria: ')
nu_ho_tr = float(input('Informe o número de horas trabalhadas no més: '))
if turno == 'M':
     coeficiente = 10/100 * sal_min
if turno == 'V':
     coeficiente = 15/100 * sal_min
if turno == 'N':
     coeficiente = 12/100 * sal_min
print('coeficiente do salário: ',coeficiente)
sal_bruto = nu_ho_tr * coeficiente
print('Salario bruto: ',sal_bruto)
 
if categ == 'O':
    if sal_bruto >= 300:
        imposto = 5/100 * sal_bruto
    else:
        imposto = 3/100 * sal_bruto
else:
    if sal_bruto >= 400:
        imposto = 6/100 * sal_bruto
    else:
         imposto = 4/100 * sal_bruto
print('Imposto: ',imposto)
 
if turno == 'N' and nu_ho_tr > 80:
    gratificacao = 50
else:
    gratificacao = 30
print('Gratificação: ',gratificacao)
 
if categ =='O' or coeficiente <= 25:
    auxilio = 1/3 * sal_bruto
else:
    auxilio = 1/2 * sal_bruto
print('Auxilio: ',auxilio)
salario_liquido = sal_bruto - imposto + gratificacao + auxilio
print('Salário liquido: ',salario_liquido)
 
if salario_liquido < 350:
     print('Mal Remunerado')
if salario_liquido >= 350 and salario_liquido <= 600:
     print('Normal')
if salario_liquido > 600:
     print('Bem Remunerado')
