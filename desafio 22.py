nomes = str(input('DIGITE SEU NOME: ')).strip()#strip é pra tirar os espaços colocados no comeco e no fim
print(nomes)
print('Seu nome em maiusculo: {}'.format(nomes.upper()))
print('Seu nome em minusculo: {}'.format(nomes.lower()))
print('Seu nome tem {} letras '.format(len(nomes)-nomes.count(' ')))# len vai dar a quantidade de letras e o menos count vai tirar os espaços
separa = nomes.split() # vai separar os nomes
print('Seu primeiro nome é {} e tem {} letras '.format(separa[0], len(separa[0]))) # vai mostrar a posição zero do nome que e o primeiro e depois vai contar quantas letras tem
