'''Faça um programa que receba o código correspondente ao cargo de um
funcionário e seu salário atual e mostre o cargo, o valor do aumento e seu
novo salário. Os cargos estão na tabela a seguir.
CÓDIGO | CARGO        | PERCENTUAL
1      | Escriturário | 50%
2      | Secretário   | 35%
3      | Caixa        | 20%
4      | Gerente      | 10%
5      | Diretor      | Não tem aumento'''

print('1: Escriturário, 2: Secretário, 3: Caixa, 4: Gerente, 5: Diretor')
cargo = int(input('Informe o seu código de cargo: '))
while(cargo > 5):
    print('ERRO: Cargo nao existe.')
    cargo = int(input('Informe o seu código de cargo novamente: '))
salario = float(input('Informe o se salário: '))
if cargo == 1:
    print('O cargo é Escriturário')
    aumento = salario * 50 / 100
    print('O valor do aumento é: ',aumento)
    novo_sal = salario + aumento
    print('O novo salário é: ', novo_sal)
elif cargo == 2:
    print('O cargo é Secretário')
    aumento = salario * 35 / 100
    print('O valor do aumento é: ',aumento)
    novo_sal = salario + aumento
    print('O novo salário é: ', novo_sal)
elif cargo == 3:
    print('O cargo é Caixa')
    aumento = salario * 20 / 100
    print('O valor do aumento é: ',aumento)
    novo_sal = salario + aumento
    print('O novo salário é: ',novo_sal)
elif cargo == 4:
    print('O cargo é Gerente')
    aumento = salario * 10 / 100
    print('O valor do aumento é: ',aumento)
    novo_sal = salario + aumento
    print('O novo salário é: ',novo_sal)
else:
    print('O cargo é Diretor')
    aumento = salario * 0 / 100
    print('O valor do aumento é: ',aumento)
    novo_sal = salario + aumento
    print('O novo salário é: ',novo_sal)