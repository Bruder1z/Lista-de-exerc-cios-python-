a = int(input('Dias alugados: '))
k = float(input('Quantos km rodados: '))
f = (60 * a) + (k * 0.15)
print('O total a pagar é R${} '.format(f))