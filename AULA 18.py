#teste = list()
#teste.append('Lucas')
#teste.append(19)
#galera = list()
#galera.append(teste[:])
#teste[0] = 'MARIA'
#teste[1] = 22
#galera.append(teste[:])
#print(galera)

#galera = [['MENDES', 19], ["LUCAS", 18], ['LUIZA', 12], ['DAVI', 7]]
#print(galera)
#print(galera[0][0])
#for p in galera:
    #print(p)

galera = list()
dado = list()
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
