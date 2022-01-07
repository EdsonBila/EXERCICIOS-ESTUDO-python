'''Um funcionário de uma empresa recebe, anualmente, aumento salarial.
    Sabe-se que:
        Esse funcionário foi contratado em 2005, com salário inicial de R$ 1.000,00.
        Em 2006, ele recebeu aumento de 1,5% sobre seu salário inicial.
        A partir de 2007, os aumentos salariais sempre corresponderam ao dobro do percentual
        do ano anterior.
    Faça um programa que determine o salário atual desse funcionário.'''

ano_atual = int(input('Informe o ano atual: '))

salario_inicial = 1000
percentual_do_ano = 1.5 / 100
aumento_do_ano = salario_inicial * percentual_do_ano
salario_do_ano = salario_inicial + aumento_do_ano

for contador in range(2007,ano_atual + 1):
    percentual_do_ano = percentual_do_ano * 2
    aumento_do_ano = salario_do_ano * percentual_do_ano
    salario_do_ano = salario_do_ano + aumento_do_ano
    
print('Ano', salario_do_ano)