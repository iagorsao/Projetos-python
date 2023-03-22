velocidade = float(input('Qual a velocidade do carro?: '))
if velocidade > 80:
    print('VOCE FOI MULTADO!')
else:
    print('PODE FICAR TRANQUILO !')
if velocidade > 80:
    print('O VALOR DA MULTA É DE',(velocidade - 80) * 7)
