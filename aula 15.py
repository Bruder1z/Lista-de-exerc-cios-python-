n = s = 0
while n != 999:
   n = int(input("DIGITE UM NÚMERO: "))
   if n == 999:
       break
   s += n
print("A soma vale {}".format(s))
print("ACABOU")