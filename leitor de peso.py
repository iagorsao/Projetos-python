maior = 0
menor = 0
for c in range(1,6):
    print('--=' * 20)
    peso = float(input('PESO DA {} PESSOA: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if  peso < menor:
            menor = peso
print('O maior peso lido foi de {} kg'.format(maior))
print('O menor peso lido foi de {} kg'.format(menor))