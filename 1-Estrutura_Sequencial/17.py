''' Um trabalhador recebeu seu salário e o depositou em sua conta bancária. Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. O banco criou uma taxa para a operação bancária de retirada que tem que pagar um imposto, chamado de cpmf, de 0.38% e o saldo inicial da conta está zerado'''
salario = float(input('Digite o seu salário: '))
valor_cheque1 = float(input('Digite o valor do cheque: '))
valor_cheque2 = float(input('Digite o valor do cheque: '))
cpmf_cheque1 = (valor_cheque1 * 0.038) / 100
saque1 = valor_cheque1 + cpmf_cheque1
cpmf_cheque2 = (valor_cheque2 * 0.038) / 100
saque2 = valor_cheque2 + cpmf_cheque2
saldo = salario - saque1 - saque2
print('Seu saldo: ',saldo)