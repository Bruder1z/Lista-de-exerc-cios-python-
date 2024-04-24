from random import randint
v = 0
while True:
    jogador = int(input("DIGA UMA VALOR: "))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
       tipo = str(input("PAR OU ÍMPAR: [P/N] ")).strip().upper()[0]
    print("VOCÊ JOGOU {} E O PC JOGOU {}.TOTAL DE {}".format(jogador, pc, total))
    if tipo == 'P':
        if total % 2 == 0:
            print("GANHOU")
            v += 1
        else:
            print("PERDEU")
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print("GANHOU")
            v += 1
        else:
            print('PERDEU')
            break

    print("TRY AGAIN?")
print("GAME OVER! VC VENCEU {} VEZES".format(v))