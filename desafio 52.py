num = int(input('DIGITE UM NÚMERO: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m0 NÚMERO {} FOI DIVISIVEL {} VEZES'.format(num, tot))
if tot == 2:
    print('POR ISSO ELE É PRIMO')
else:
    print('E POR ISSO ELE NAO É PRIMO')
