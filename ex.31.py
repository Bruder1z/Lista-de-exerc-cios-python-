d = int(input("Qual a distãncia da sua viagem? "))

if d <= 200:
    var = d * 0.50
    print("O valor da viagem foi de {}".format(var))
else:
    new = d * 0.45
    print("O  valor da viagem foi de {}".format(new))
