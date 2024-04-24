from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 8):
    atual = date.today().year
    ano = int(input('EM QUE ANO A {} PESSOA NASCEU? '.format(pess)))
    idade = atual - ano
    if idade >= 21:
      totmaior += 1
    else:
      totmenor += 1
print('AO TODO TIVEMOS {} PESSOAS MAIORES DE IDADE'.format(totmaior))
print('AO TODO TIVEMOS {} PESSOAS MAIORES DE IDADE'.format(totmenor))

