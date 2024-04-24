a = int(input("Digite um valor:  "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor:  "))

if a < b + c and b < a + c and c < a + b:
    print("PODE FORMAR UM TRIANGULO")
else:
    print("Não pode formar um triangulo")
