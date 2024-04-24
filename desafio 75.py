num = (int(input("Digite um numero: ")),
       int(input("Digite um numero: ")),
       int(input("Digite um numero: ")),
       int(input("Digite um numero: ")))
print("Você digitou os valores {}".format(num))
print("O valor 9 apareceu {} vezes".format(num.count(9)))
if 3 in num:
    print("O valor 3 apareceu ma {} posição".format(num.index(3)+1))
else:
    print("O valor 3 nao foi digitado")
for n in num:
    if n % 2 == 0:
        print(n)
