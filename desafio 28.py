from random import randint
pc = randint(0, 5)
print("pensei no número {} ".format(pc))
print("Vou pensar em um numero entre 0 e 5")
jogador = int(input("Em qual número pensei? "))
if jogador == pc:
    print("VOCE VENCEU")
else:
    print('Voce perdeu')
    print("Eu pensei no numero {}".format(pc))
