import math
co = float(input('Qual é o comprimento do Cateto oposto? '))
ca = float(input('Qual é o comprimento do cateto adjacente? '))
hi = math.hypot(co, ca)
print('A hipotenusa vai meidir {:.2f}'.format(hi))
