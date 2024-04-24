total = totmil = menor = cont = 0
while True:
    nome = str(input("NOME DO PRODUTO: "))
    P = float(input("QUAL O PREÇO? R$: "))
    cont += 1
    total += P
    if P > 1000:
        totmil += 1
    if cont ==1:
        menor = P
    else:
        if P < menor:
            menor = P
    r = ' '
    while r not in 'SN':
        r = str(input("CONTINUAR? [S-N]")).strip().upper()[0]
    if r == 'N':
        break
print("TOTAL = {} ".format(total))
print("PRODUTOS QUE VALEM MAIS DE MIL REAIS {}".format(totmil))
print("FIM DO PROGRAMA")
print("PRODUTO MAIS BARATO CUSTA R$ {}".format(menor))