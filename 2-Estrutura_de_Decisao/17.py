'''Faça um programa que receba a hora do início de um jogo e a hora do
término (cada hora é composta por duas variáveis inteiras: hora e minuto).
Calcule e mostre a duração do jogo (horas e minutos), sabendo que o tempo
máximo de duração do jogo é de 24 horas e que ele pode começar em um
dia e terminar no dia seguinte.'''

hi = int(input('hora inicial do jogo: '))
if hi > 24:
    print('esse formato de hora não existe')
else:
    mi = int(input('minuto inicial do jogo: '))
    if mi > 59:
        print('esse formato de minuto não existe')
    else:
        hf = int(input('hora final do jogo: '))
        if hf > 24:
            print('esse formato de hora não existe')
        else:
            mf = int(input('minuto final do jogo: '))
            if mf > 59:
                print('esse formato de minuto não existe')
            else:
                if hi < hf:
                    if mi > mf:
                        hj = hf - 1 - hi
                        mj = mf + 60 - mi
                    else:
                        hj = hf - hi
                        mj = mf - mi
                elif hi > hf:
                    if mi > mf:
                        hj = hf + 23 - hi
                        mj = mf + 60 - mi
                    else:
                        hj = hf + 24 - hi
                        mj = mf - mi
                else:
                    if mi > mf:
                        hj = hf + 23 - hi
                        mj = mf + 60 - mi
                    else:
                        hj = hf - hi
                        mj = mf - mi
print('tempo de jogo: ',hj,'hr',mj,'min')