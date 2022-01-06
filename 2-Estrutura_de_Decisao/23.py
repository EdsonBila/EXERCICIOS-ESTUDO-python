'''Faça um programa para resolver equações do 2 o grau. ex: ax² + bx + c = 0 
 A variável a deve ser diferente de zero*
delta = b ** 2 - 4 * a * c;
delta < 0. Não existe raiz real;
delta = 0. Existe uma raiz real;
    x = (-b) / (2 * a)
delta > 0. Existem duas raízes reais;
    x1 = (-b + delta )/ (2 * a)
    x2 = (-b - delta )/ (2 * a)'''

print('ax²+bx+c=0')
a = float(input('digite o valor de a: '))
while(a == 0):
    print('Estes valores não formam uma equação de segundo grau')
    a = float(input('digite o valor de a: '))
b = float(input('digite o valor de b: '))
c = float(input('digite o valor de c: '))
delta = (b * b) - ( 4 * a * c)
if delta < 0:
    print('Não existe raiz real')
elif delta == 0:
    print('Existe uma raiz real')
    x1 = (- b) / (2 * a)
    print(x1)
elif delta > 0:
    print('Existem duas raízes reais')
    x1 = (- b) + (delta**(1/2)) / (2 * a)
    x2 = (- b) - (delta**(1/2)) / (2 * a)
    print(x1, x2)