from time import sleep

idade = int(input('Digite a sua idade: '))
genero = input(' QUAL SEU GENERO : ')
genero = 'masc'

genero = 'fem'

print('PROCESSANDO!!')
print('-=' * 20)
sleep(2)

if idade < 18 and genero == 'masc':
    tempo = (18 - idade)
    print('\033[1;33m VOCE AINDA VAI SE ALISTAR FALTAM {} ANOS \033[1;33m'.format(tempo))

elif idade == 18 and genero == 'masc' :
    print(' \033[1;32m ESTA NA HORA DE SE ALISTAR \033[1;32m')

elif idade > 18 and genero == 'masc':
    tempo = (idade - 18)
    print('\033[1;31m SEU TEMPO DE SE ALISTAR JA PASSOU {} ANOS \033[1;31m'.format(tempo))

elif genero == 'fem':
    print('VOCE NAO PRECISA')