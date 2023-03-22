from datetime import date
atual = date.today().year
nascimento = int(input('Qual seu ano de nascimento?: '))

idade = (atual - nascimento)

print('VOCE NASCEU EM {} E TEM {} ANOS'.format(nascimento, idade))

if idade <= 9:
    print('MIRIM')
elif  9 < idade <= 14:
    print('INFANTIL')

elif 14 < idade <= 19:
    print('JUNIOR')

elif 19 < idade <= 25:
    print('SENIOR')

elif 25 < idade :
    print('MASTER')
