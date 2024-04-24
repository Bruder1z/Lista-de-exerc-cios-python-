n = float(input('fale o preço do produto? R$'))
nv = n - (n*5 / 100)
print('O produto que custava {:.2f}, na promoção vai custar {:.2f}'.format(n, nv))