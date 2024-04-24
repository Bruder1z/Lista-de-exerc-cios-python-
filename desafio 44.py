print('LOJAS BRUDER')
preco = float(input('PREÇO DAS COMPRAS: '))
print(''' FORMAS DE PAGAEMNTO
[1] À VISTA DINHEIRO/CHEQUE
[2] À VISTA CARTÃO 
[3] 2X NO CARTÃO 
[4] 3X OU MAIS NO CARTÃO ''')

opcao = int(input('Qual é a opcao? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('SUA COMPRA SAIRA POR {}'.format(total))


elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('SUA COMPRA SAIRA POR {}'.format(total))

elif opcao == 3:
    total = preco
    parcela = total/2
    print('SUA COMPRA SERÁ PARCELADA 2x de R$ {:2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    tp = int(input('Quantas parcelas? '))
    parcela = total / tp
    print('SUA COMPRA SERÁ PARCELADA {}x DE R$ {:2f} COM JUROS'.format(tp, parcela))
    print('SUA COMPRA DE R${:2f} VAI CUSTAR R${:.2f} no final.'.format(preco, total))

else:
    total = preco
    print('OPCAO INVALIDA')