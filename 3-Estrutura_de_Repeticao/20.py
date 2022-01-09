'''Faça um programa que receba o valor de uma dívida e mostre uma
tabela com os seguintes dados:
    valor da dívida,
    valor dos juros,
    quantidade de parcelas
    valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela:
    Quantidade de parcelas | % de juros sobre o valor inicial da dívida
    1                      | 0
    3                      | 10
    6                      | 15
    9                      | 20
    12                     | 25
Exemplo de saída do programa:
    Valor da dívida | Valor dos juros (em reais) | Quantidade de parcelas | Valor da parcela
    1.000,00        | 0                          | 1                      | 1.000,00
    1.100,00        | 100                        | 3                      | 366,67
    1.150,00        | 150                        | 6                      | 191,67'''

c = 'S'
while c == 'S':
  divida = int(input('Digite o valor da dívida R$: '))
  parcelas = 1
  print('')
  print('Formas de pagamento:')
  print('Valor da dívida | Valor dos juros R$ | Quantidade de parcelas | Valor da parcela')
  while parcelas <= 12:
    if parcelas == 1:
      j = 0
      juros = divida*(j/100) 
      v = (divida + juros)/parcelas
    print(f'{divida}                 {juros:.2f}                  {parcelas}                          {v:.2f}') 
    parcelas += 2    
    if parcelas == 3:
      j = 10 
      juros = divida*(j/100) 
      v = (divida + juros)/parcelas
    print(f'{divida}                 {juros:.2f}                  {parcelas}                          {v:.2f}')  
    j += 5  
    parcelas += 3
    juros = divida*(j/100) 
    v = (divida + juros)/parcelas
  print('') 
  c = input('Quer negociar outra dívida?: ').upper()
print('até mais')  