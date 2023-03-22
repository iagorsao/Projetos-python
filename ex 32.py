ano = int(input('Digite o ano aqui: ')) #ano bissexto 
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(' ano bissesto')
else:
    print('nao e nd')