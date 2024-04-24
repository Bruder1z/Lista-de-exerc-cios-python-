from math import factorial
fat = int(input('DIGITE UM NÚMERO PARA SABER SEU FATORIAL: '))
f = factorial(fat)
print('O fatorial de {} é {}'.format(fat, f))

#modo tradicional#

n = int(input('DIGITE UM NÚMERO PARA SABER SEU FATORIAL: '))
c = n
v = 1
print('Calculando...')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    v *= c
    c -= 1
print('{}'.format(v))