tot = 0
n = int(input('DIGITE UM NUMERO :'))
for c in range(1 , n + 1):
    if n % c == 0:
        print('\033[33m', end=' ' )
        tot = tot + 1
    else:
        print('\033[31m', end=' ' )

    print('{}'.format(c), end=' ')
print('\n\033[mo numero {} foi divisivel {} vezes '.format(n, tot))
if tot == 2:
    print('e primo')
else:
    print('nao e primo')