n1 = int(input('DIGITE O PRIMEIRO NUMERO: '))

n2 = int(input('DIGITE O SEGUNDO NUMERO: '))

print('-=' * 20)

if n1 == n2:
    print('\033[0;33m OS DOIS VALORES SÃO IGUAIS!!! \033[0;33m')

elif n1 > n2:
    print('\033[0;34m O PRIMEIRO VALOR É MAIOR \033[0;34m')

else:
    print('\033[0;36m O SEGUNDO VALOR É MAIOR \033[0;36m')

print('_=' * 20)

print('FIM')
