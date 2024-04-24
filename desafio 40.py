n1 = float(input("Qual foi sua primeira nota: "))
n2 = float(input("Qual foi sua segunda nota: "))
media = (n1 + n2)/2

if 7 > media >= 5:
    print('RECUPERAÇÃO!')
elif media < 5:
    print('REPROVADO!')
elif media >= 7:
    print('APROVADO!')