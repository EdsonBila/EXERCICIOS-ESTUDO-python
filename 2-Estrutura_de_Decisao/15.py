'''Faça um programa que mostre a data e a hora do sistema nos seguintes
formatos: DD/MM/AAAA – mês por extenso e hora:minuto.'''

from datetime import datetime
hoje = datetime.now()
if hoje.month == 1:
    mes = 'janeiro'
    hora = hoje.hour - 3
    print(hoje.day,'/',mes,'/',hoje.year)
    print(hoje.hour,':',hoje.minute)
    print(hoje.second,'segundos')
elif hoje.month == 2:
    mes = 'fevereiro'
    hora = hoje.hour - 3
    print(hoje.day,'/',mes,'/',hoje.year)
    print(hoje.hour,':',hoje.minute)
    print(hoje.second,'segundos')
elif hoje.month == 3:
    mes = 'março'
    hora = hoje.hour - 3
    print(hoje.day,'/',mes,'/',hoje.year)
    print(hoje.hour,':',hoje.minute)
    print(hoje.second,'segundos')
elif hoje.month == 4:
    mes = 'abril'
    hora = hoje.hour - 3
    print(hoje.day,'/',mes,'/',hoje.year)
    print(hoje.hour,':',hoje.minute)
    print(hoje.second,'segundos')
elif hoje.month == 5:
    mes = 'maio'
    hora = hoje.hour - 3
    print(hoje.day,'/',mes,'/',hoje.year)
    print(hoje.hour,':',hoje.minute)
    print(hoje.second, 'segundos')
elif hoje.month == 6:
    mes = 'junho'
    hora = hoje.hour - 3
    print(hoje.day,'/',mes,'/',hoje.year)
    print(hoje.hour,':',hoje.minute)
    print(hoje.second,'segundos')
elif hoje.month == 7:
    mes = 'julho'
    hora = hoje.hour - 3
    print(hoje.day,'/',mes,'/',hoje.year)
    print(hoje.hour,':',hoje.minute)
    print(hoje.second,'segundos')
elif hoje.month == 8:
    mes = 'agosto'
    hora = hoje.hour - 3
    print(hoje.day,'/',mes,'/',hoje.year)
    print(hoje.hour,':',hoje.minute)
    print(hoje.second,'segundos')
elif hoje.month == 9:
    mes = 'setembro'
    hora = hoje.hour - 3
    print(hoje.day,'/',mes,'/',hoje.year)
    print(hoje.hour,':',hoje.minute)
    print(hoje.second,'segundos')
elif hoje.month == 10:
    mes = 'outubro'
    hora = hoje.hour - 3
    print(hoje.day,'/',mes,'/',hoje.year)
    print(hoje.hour,':',hoje.minute)
    print(hoje.second,'segundos')
elif hoje.month == 11:
    mes = 'novembro'
    hora = hoje.hour - 3
    print(hoje.day,'/',mes,'/',hoje.year)
    print(hoje.hour,':',hoje.minute)
    print(hoje.second,'segundos')
elif hoje.month == 12:
    mes = 'dezembro'
    hora = hoje.hour - 3
    print(hoje.day,'/',mes,'/',hoje.year)
    print(hoje.hour,':',hoje.minute)
    print(hoje.second,'segundos')
