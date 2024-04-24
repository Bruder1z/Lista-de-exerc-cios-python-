t1 = float(input('tamamho do primeiro triangulo: '))
t2 = float(input('tamamho do segundo triangulo: '))
t3 = float(input('tamamho do terceiro triangulo: '))

if t1 == t2 and t3 == t1:
     print('TRIANGULO EQUILATERO')

elif t1 != t2 and t2 == t3:
    print('TRIANGULO ISOSCELES')

elif t2 != t3 and t1 == t3:
    print('TRIANGULO ISOSCELES')

else:
    print('TRIANGULO ESCALENO')
