''' Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio no último ano. Faça um algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir. Mostre uma mensagem informando o saldo médio e o valor do crédito. Saldo médio de 0 a 200 nenhum crédito; de 201 a 400 20% do valor do saldo médio; de 401 a 600 30% do valor do saldo médio; acima de 601 40% do valor do saldo médio.'''

saldo_medio = float(input('Informe o saldo médio: '))
if saldo_medio >=0 and saldo_medio <=200:
    print('Saldo médio: ',saldo_medio)
    print('Crédito: nenhum crédito')
elif saldo_medio >=201 and saldo_medio <=400:
    valor_do_credito1 = saldo_medio * 20 / 100
    print('Saldo médio: ',saldo_medio)
    print('Crédito: ',valor_do_credito1)
elif saldo_medio >=401 and saldo_medio <=600:
    valor_do_credito2 = saldo_medio * 30 / 100
    print('Saldo médio: ',saldo_medio)
    print('Crédito: ',valor_do_credito2)
else:
    valor_do_credito3 = saldo_medio * 40 /100
    print('Saldo médio: ',saldo_medio)
    print('Crédito: ',valor_do_credito3)
