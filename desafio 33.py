a = int(input("Digite um valor:  "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor:  "))

menor = a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

maior = a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print("O MAIOR VALOR FOI {}".format(maior))
print("O MENOR VALOR FOI {}".format(menor))