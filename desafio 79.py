números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print("Valor recebido com sucesso")
    else:
        print('VALOR DUPLICADO')

    r = str(input('Quer Continuar? [S/N]'))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os vlores {números}')
