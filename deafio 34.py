salario = float(input('QUAL VALOR DO SEU SALARIO? '))
if salario > 1250:
    maior = (salario*10)/100
    print('com seu aumento seu salario vai ser de {:.2f} R$'.format(salario+maior))
else:
    menor = (salario*15)/100
    print('com seu aumento seu salario vai ser de {:.2f} R$'.format(salario+menor))