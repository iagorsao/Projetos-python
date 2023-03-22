nota1 = float(input('DIGITE A PRIMEIRA NOTA: '))
nota2 = float(input('DIGITE A SEGUNDA NOTA: '))
media = (nota1 + nota2)/2

print(media)

if media < 5:
    print(' \033[1;31m REPROVADO \033[1;31m')

elif media >= 5.0 and media < 7:
    print('\033[1;36m RECUPERAÇÃO \033[1;36m')

elif media > 7:
    print('\033[1;32m APROVADO \033[1;32m')

