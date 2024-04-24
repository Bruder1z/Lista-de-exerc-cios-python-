from datetime import date
atual = date.today().year
born = int(input('Que ano voce nasceu? '))
age = atual - born
print('Quem nasceu em {} tem {} anos em {}.'.format(born, age, atual))
if age == 18:
 print("ALISTAMENTO MILITAR OBRIGATORIO")
elif age < 18:
    saldo = 18 - age
    print('Voce ainda nao tem 18 anos. Ainda faltam {} para o alistamento militar obrigatorio '.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif age > 18:
    saldo = age - 18
    print('Voce já devia ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))