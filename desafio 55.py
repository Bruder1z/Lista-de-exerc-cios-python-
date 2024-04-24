maior = 0
menor = 0
for c in range (1, 6):
    weight = float(input('DIGITE O PESO DA {} PESSOA: '.format(c)))
    if c == 1:
        maior = weight
        menor = weight
    else:
        if weight > maior:
            maior = weight
        if weight < menor:
            menor = weight
print('O MAIOR PESO LIDO FOI DE {}KG'.format(maior))
print('O MENOR PESO LIDO FOI DE {}KG'.format(menor))
