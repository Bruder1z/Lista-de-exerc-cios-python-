soma = 0
cont = 0
for c in range (1, 7):
    num = int(input('DIGITE UM NÚMERO: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('VOCÊ INFORMOU {} NÚMEROS PARES E A SOMA FOI {}'.format(cont, soma))

