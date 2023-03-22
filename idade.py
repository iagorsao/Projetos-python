from datetime import date
atual = date.today().year
contador1 = 0
contador2 = 0
for c in range(1, 8):
    idade = int(input('DIGITE EM QUE ANO VOCÊ NASCEU: '))
    id = atual-idade

    if id >= 18:
        contador1 = contador1 + 1
        print('\033[32m',id, '\033[32m')
    else:
        contador2 = contador2 + 1
        print('\033[31m',id, '\033[31m')

print('{} PESSOAS SAO DE MAIOR E {} PESSOAS SÂO DE MENOR'.format(contador1, contador2))
