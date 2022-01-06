'''A nota nal de um estudante é calculada a partir de três notas atribuídas,
respectivamente, a um trabalho de laboratório, a uma avaliação semestral e
a um exame nal. A média das três notas mencionadas obedece aos pesos
a seguir: 
NOTA                    |PESO
Trabalho de laboratório |2
Avaliação semestral     |3
Exame nal               |5
Faça um programa que receba as três notas, calcule e mostre a média
ponderada e o conceito que segue a tabela:
MÉDIA PONDERADA     | CONCEITO
8,0 <= média <= 10  | A
7,0 <= média < 8,0  | B
6,0 <= média < 7,0  | C
5,0 <= média < 6,0  | D
0,0 <= média < 5,0  | E
media_ponderada = (nota_traballho * 2 + avaliacao_semestral * 3 + exame_nal * 5) / 10'''

tr_laboratorio = float(input('Informe a nota do trabalho de laboratório: '))
av_semestral = float(input('Informe a nota da avaliação semestral: '))
ex_final = float(input('Informe a nota do exame final: '))
media_ponderada = (tr_laboratorio*2 + av_semestral*3 + ex_final*5) / 10
if media_ponderada >= 8.0 and media_ponderada <= 10:
    print('Média ponderada: ',media_ponderada)
    print('Conceito: A')
elif media_ponderada >= 7.0 and media_ponderada < 8.0:
    print('Méddia ponderada: ',media_ponderada)
    print('Conceito: B')
elif media_ponderada >= 6.0 and media_ponderada < 7:
    print('Média ponderada: ',mediapo_nderada)
    print('Conceito: C')
elif media_ponderada >= 5.0 and media_ponderada < 6.0:
    print('Média ponderada: ',media_ponderada)
    print('Conceito: D')
else:
    print('Média ponderada: ',media_ponderada)
    print('Conceito: E')