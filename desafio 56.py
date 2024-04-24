somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print('------{} pesssoa ------'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = nome
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade/4
print('A MEDIA DE IDADE DO GRUPO É DE {} ANOS'.format(mediaidade))
print('O HOMEM MAIS VELHO TEM {} ANOS E SE CHAMA {}'.format(maioridadeh, nomevelho))
print('AO TODO SÃO {} MULHERES COM MENOS DE 20 ANOS'.format(totmulher20))