num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
if num1 > num2:
    print('o numero {} é maior que o numero {}'.format(num1, num2))
elif num2 > num1:
    print('O numero {} é maior que o numero {}'.format(num2, num1))
else:
    print('Os números são iguais!')
