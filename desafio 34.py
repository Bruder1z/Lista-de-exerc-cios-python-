s = int(input('Qual o seu salario? '))
if s >1250:
    n = s + ( s * 10)/100
    print("SEU NOVO SALARIO É DE {} ".format(n))
else:
    m = s + (s*15)/100
    print("SEU NOVO SALÁRIO É DE {} ".format(m))
