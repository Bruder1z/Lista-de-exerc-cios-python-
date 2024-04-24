tot18 = toth = totm20 = 0
while True:
    idade = int(input("IDADE: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("SEXO: [M/F]")).strip().upper()[0]
    if idade >= 18:
        tot18 +=1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    r = ' '
    while r not in 'SN':
        r = str(input("Quer continuar? ")).strip().upper()[0]
    if r == 'N':
         break
print("TOTAL DE PESSOAS COM MAIS DE 18 ANOS: {}".format(tot18))
print("TOTAL DE HOMENS CADASTRADOS: {} ".format(toth))
print("TOTAL DE MULHERES COM MAIS DE 20 ANOS: {}".format(totm20))