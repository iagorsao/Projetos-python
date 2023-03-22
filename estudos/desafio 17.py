import math
c1 = float(input(' Valor do  cateto oposto: ' ))
c2 = float(input('Valor do cateto adjacente: '))
hi = math.hypot(c1,c2)
print('O compimento da hipotenusa é {:.2f}'.format(hi))