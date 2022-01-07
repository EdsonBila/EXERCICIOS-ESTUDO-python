'''Faça um programa que monte os oito primeiros termos da sequência de
Fibonacci.'''

numero_elementos_sequencia = 9
elementoN = 1
elementoNmais1 = 1

print(elementoN)
print(elementoNmais1)
 
for elemento in range(3,numero_elementos_sequencia):
    valor_do_fibonacci_atual = elementoN + elementoNmais1
 
    print(valor_do_fibonacci_atual)
 
    elementoN = elementoNmais1
    elementoNmais1 = valor_do_fibonacci_atual