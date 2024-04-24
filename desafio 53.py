nome = str(input('DIGITE UMA FRASE: ')).strip().upper()
palavras = nome.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('A FRASE DIGITADA NÃO É UM PALÍNDROMO')



