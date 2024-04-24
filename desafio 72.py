cont = ("zero", 'um', 'dois', 'tres', "quatro",
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'Quinze', 'Dezesseis', 'dezessete', 'Dezoito',
        'Dezenove', 'Vinte')
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        break
    print("Tente novamente> ", end='')
print(f'voce digitou o numero:{cont[num]}')

