''' Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem constante na tabela a seguir. Aos alunos que caram para exame, calcule e mostre a nota que deverão tirar para
serem aprovados, considerando que a média exigida é 6,0.
MÉDIA ARITMÉTICA    | MENSAGEM
0,0 <= média < 3,0  | Reprovado
3,0 <= média < 7,0  | Exame
7,0 <= média <= 10,0| Aprovado'''

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunnda nota: '))
nota3 = float(input('Informe a terceira nota: '))
media = round(nota1 + nota2 + nota3) / 3

if media <= 0.0 and media < 3.0:
    print('Reprovado')
    print('Média aritmética: ',media)
elif media == 3.0 and media < 7.0:
    print('Exame')
    print('Média aritmética: ',media)
elif media >= 7.0 and media <= 10.0:
    print('Aprovado')
    print('Média aritmética: ',media)
else:
    media >= 3 and media < 7
    print('Exame')
    nota_exame = 12 - media
    print('Deve tirar nota: ',nota_exame,'para ser aprovado')
