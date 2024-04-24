import random
from time import sleep
itens =('Pedra', 'Papel', 'Tesoura')
comp = random.randint(0, 2)

opc = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
print('JO')
sleep(0.3)
print('KEN')
sleep(0.3)
print('PO!')
print('=' * 10)
print(f'Computador jogou {itens[comp]}.')
print(f'Você jogou {itens[opc]}.')
if comp == 0:
    if opc == 0:
        print('EMPATE!')
    elif opc == 1:
        print('VOCÊ VENCEU!')
    elif opc == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('ESCOLHA INVÁLIDA.')

elif comp == 1:
    if opc == 0:
        print('COMPUTADOR VENCEU!')
    elif opc == 1:
        print('EMPATE!')
    elif opc == 2:
        print('VOCÊ VENCEU!')
    else:
        print('ESCOLHA INVÁLIDA.')

elif comp == 2:
    if opc == 0:
        print('VOCÊ VENCEU!')
    elif opc == 1:
        print('COMPUTADOR VENCEU!')
    elif opc == 2:
        print('EMPATE!')
    else:
        print('ESCOLHA INVÁLIDA.')

print('=' * 10)