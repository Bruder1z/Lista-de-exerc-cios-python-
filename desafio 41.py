from datetime import date
atual = date.today().year
ano = int(input('ano de nasciemnto: '))
idade = atual - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print("atleta MIRIM")
elif 9 < idade  <=14 :
    print('atleta INFANTIL')
elif 14 < idade <= 19:
    print('atleta JUNIOR')
elif 19 < idade <= 25:
    print('atleta SENIOR')
else:
    print('atleta MASTER')
