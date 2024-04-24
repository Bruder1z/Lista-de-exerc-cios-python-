times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético MG', 'Botafogo', 'Athletico', 'Bahia',
         'São paulo', 'Fluminense', 'Sport', 'Vitória',
         'Coritiba', 'Avaí', 'Ponte Peta', 'Atletico-GO')
print('-=' * 15)
print("Lista de times -> {} ".format(times))
print('-=' * 15)
#for t in times:
    #print(t)
print('-=' * 15)
print('os 5 primeiros times são {}'.format(times[0:5]))
print('-=' * 15)
print('Os últimos 4 colocados sao {}'.format(times[-4:]))
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print('O TIME DA CHAPE ESTÁ NA POSIÇÃO {times.index("Chapecoense")+1}')