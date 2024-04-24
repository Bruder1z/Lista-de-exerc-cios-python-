n1 = int(input('PRIMIERO VALOR: '))
n2 = int(input('SEGUNDO VALOR: '))
opção = 0
while opção != 5:


    print('''    [1] SOMAR
    [2] multiplicar 
    [3] maior 
    [4] novos números
    [5] sair do programa''')
    opção = int(input('Qual a sua opção: '))
    if opção == 1:
        soma = n1 + n1
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        vezes = n1 * n2
        print('A  multiplicação entre {} e {} da {}'.format(n1, n2, vezes))
    elif opção == 3:
            if n1 > n2:
                maior = n1
            else:
                maior = n2
            print('Entre os dois números o maior é {}'.format(maior))
    elif opção == 4:
        print('INFORME OS NÚMEROS NOVAMENTE: ')
        n1 = int(input('PRIMEIRO VALOR: '))
        n2 = int(input('SEGUNDO VALOR: '))
    elif opção == 5:
        print('FINALIZANDO...')
    else:
        print('Opção invalida')
    print('FIM DO PROGRAMA')
