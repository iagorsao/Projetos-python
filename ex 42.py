peso = float(input('DIGITE SEU PESO: '))

altura = float(input('DIGITE SUA ALTURA: '))

imc = peso / (altura ** 2)

print('SEU IMC È DE {:.2f}'.format(imc))

if imc < 18.5:
    print('ABAIXO DO PESO')
elif  18.5 <= imc and imc <= 25 :
    print('PESO IDEAL')
elif 26 <= imc <= 30 :
    print('SOBREPESO')
elif  30 < imc <= 40 :
    print('OBESIDADE')
elif imc > 40:
    print('OBESIDADE MORBIDA')
