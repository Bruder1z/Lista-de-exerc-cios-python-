s = cont = 0
n = 0
while n != 999:
    n = int(input("DIGITE UM NÚMERO: "))
    if n == 999:
        break
    cont += 1
    s += n
print("A soma vale {} e foram digitados {} números".format(s, cont))