print('1O TERMOS DE UMA PA')

a1 = int(input('PRIMEIRO TERMO: '))
r = int(input('RAZÃO: '))
dez = a1 + (10 - 1) * r
for c in range (a1, dez + r, r):
    print('{}'.format(c), end=' - ')
print('END')