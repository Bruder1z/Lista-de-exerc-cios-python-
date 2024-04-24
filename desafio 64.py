num = cont = soma = 0
num = int(input('Digite um número [999 para encerrar] '))
while num != 999:
    soma = soma + num
    cont += 1
    num = int(input('Digite um número [999 para encerrar] '))
print('foram digitados {} numeros e a soma foi {} .'.format(cont, soma))
