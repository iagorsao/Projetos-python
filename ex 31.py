viagem = float(input('Qual a distancia da sua viagem?: '))
preço1 = (0.50*viagem)
preço2 = (0.45*viagem)
if viagem <= 200:
    print(' o preço da sua viagem vai ser R$',preço1)
else:
    print(' O preço da sua viagem vai ser R$',preço2)

