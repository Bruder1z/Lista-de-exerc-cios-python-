from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), )
print("eu sorteei os valores {}".format(n))
#for z in n:
#print("{}".format(n))
print("O maior valor foi {}".format(max(n)))
print("O menor valor foi {}".format(min(n)))