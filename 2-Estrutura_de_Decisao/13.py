'''Faça um programa que receba quatro valores: I, A, B e C. Desses valores,
I é inteiro e positivo, A, B e C são reais. Escreva os números A, B e C obedecendo à tabela a seguir:
Suponha que o valor digitado para I seja sempre um valor válido, ou seja, 1, 2 ou 3, e que os
números digitados sejam diferentes um do outro
VALOR DE I  | FORMA A ESCREVER
1           | A, B e C em ordem crescente.
2           | A, B e C em ordem decrescente
3           | O maior ca entre os outros dois números.'''

I = int(input('Escolha entre 1,2,3: '))
if I == 1:
    print('De valores diferentes ao A, B e C')
    a = int(input('De um valor ao A: '))
    b = int(input('De um valor ao B: '))
    c = int(input('De um valor ao C: '))
    if a == b or a == c or b == c:
        print('ERRO: De valores diferentes')
    elif a < b and a < c:
        if b < c:
            print('A ordem crescente dos números é: ',a,'-',b,'-',c)
        else:
            print('A ordem crescente dos números é: ',a,'-',c,'-',b)
    elif b < a and b < c:
        if a < c:
            print('A ordem crescente dos números é: ',b,'-',a,'-',c)
        else:
            print('A ordem crescente dos números é: ',b,'-',c,'-',a)
    else:
        if a < b:
            print('A ordem crescente dos números é: ',c,'-',a,'-',b)
        else:
            print('A ordem crescente dos números é: ',c,'-',b,'-',a)
elif I == 2:
    print('De valores diferentes ao A, B e C')
    a = int(input('De um valor ao A: '))
    b = int(input('De um valor ao B: '))
    c = int(input('De um valor ao C: '))
    if a == b or a == c or b == c:
        print('ERRO: De valores diferentes')
    elif a > b and a > c:
        if b > c:
            print('A ordem decrescente dos números é: ',a,'-',b,'-',c)
        else:
            print('A ordem decrescente dos números é: ',a,'-',c,'-',b)
    elif b > a and b > c:
        if a > c:
            print('A ordem decrescente dos números é: ',b,'-',a,'-',c)
        else:
            print('A ordem decrescente dos números é: ',b,'-',c,'-',a)
    else:
        if a > b:
            print('A ordem decrescente dos números é: ',c,'-',a,'-',b)
        else:
            print('A ordem decrescente dos números é: ',c,'-',b,'-',a)
elif I == 3:
    print('De valores diferentes ao A, B e C')
    a = int(input('De um valor ao A: '))
    b = int(input('De um valor ao B: '))
    c = int(input('De um valor ao C: '))
    if a == b or a == c or b == c:
        print('ERRO: De valores diferentes')
    elif a > b and a > c:
        print('A ordem desejada é: ',b,'-',a,'-',c)
    elif b > a and b > c:
        print('A ordem desejada é: ',a,'-',b,'-',c)
    else:
        print('A ordem desejada é: ',a,'-',c,'-',b)
else:
    print('O número tem que ser 1 - 2 ou 3')
