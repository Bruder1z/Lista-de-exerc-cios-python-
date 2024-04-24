print('CALCULO DE PA')
print('Digite 0 para encerrar.')
a1 = int(input('digite o primeiro termo:  '))
r = int(input('digite sua razão: '))
termo = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total  = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print("PROGESSÃO FINALIZADA COM {} TERMOS.".total)


