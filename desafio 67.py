while True:
    n = int(input("DIGITE UM NÚMERO: "))
    if n < 0:
        break
    for c in range(1, 11):
        print("{} x {} =   {}".format(n, c, n*c))
print("NÚMERO INVÁLIDO")