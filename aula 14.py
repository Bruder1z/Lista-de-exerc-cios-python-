'''for c in range(1, 10):
    print(c)
print('FIM')'''

c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('DIGITE UM VALOR: '))
    r = str(input('QUER CONTINUAR? [S/N]')).upper()
print('FIM')

n = 1
par = impar = 0
while n != 0:
    n = int(input('DIGITE UM VALOR: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('VOCE DIGITOU {} NÚMEROS PARES E {} NÚMEROS ÍMPARES'.format(par, impar))
print("ACABOU!")