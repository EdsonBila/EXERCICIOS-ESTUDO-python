'''Faça um programa que receba três números e mostre-os em ordem crescente. Suponha que o usuário digitará três números diferentes.'''

print('Digite três números')
n1 = float(input('De um valor ao primeiro número: '))
n2 = float(input('De um valor ao segundo número: '))
n3 = float(input('De um valor ao terceiro número: '))
if n1 <= n2 and n2 <= n3:
    print('A ordem crescente: ', n1, n2, n3)
elif n1 <= n3 and n3 <= n2:
    print('A ordem crescente: ', n1, n3, n2)
elif n2 <= n1 and n1 <= n3:
    print('A ordem crescente: ', n2, n1, n3)
elif n2 <= n3 and n3 <= n1:
    print('A ordem crescente: ', n2, n3, n1)
elif n3 <= n1 and n1 <= n2:
    print('A ordem crescente: ', n3, n1, n2)
else:
    n3 <= n2 and n2 < n1
    print('A ordem crescente: ', n3, n2, n1)