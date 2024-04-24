n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('digite a sua segunda nota: '))
m = (n1+n2)/2
print("Sua media foi {:.1f}".format(m))
if m >= 6.0:
    print('Você esta aprovado')
else:
    print("Sua media foi abaixo. Está de REC")
