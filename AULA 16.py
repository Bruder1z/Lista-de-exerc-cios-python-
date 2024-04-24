lanche = ('burguer', 'juice', 'Pizza', 'cake')
print(lanche[1])

#CASO 1
#for cont in range(0, len(lanche)):
#print(lanche[cont])

#CASO 2
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

#CASO PRECISE MOSTRAR A POSIÇÃO
#FOR CONT IN RANGE (O, LEN(LANCHE)):
#PRINT(F'EU VOU COMER{COMIDA}')
#OU
#FOR POS, COMIDA IN ENUMERATE(LANCHE):
#PRINT(F'EU VOU COMER {COMIDA} NA POSIÇÃO {POS}')

#Sorted mostra em ordem
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 2, 1)
c = a + b#2,5,4,8,1,2, ordem influencia b + a não é igual a A + B
print(len(c))
print(c.count(5))#count quantas vezes aparece o numero 5(2)
print(c.index(8))#mostra qual posição esta o 8

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)#DEL APAGA DA MEMORIA
print(pessoa)

