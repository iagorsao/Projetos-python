c = 2
soma = 0
div = 0
while c < 3:
    var1 = int(input('DIGITE O PRIMEIRO VALOR: '))
    var2 = int(input('DIGITE O SEGUNDO VALOR : '))
    print(''' QUAL OPERAÇÂO VOCE DESEJA
[1] somar
[2]multiplicar
[3]Maior 
[4]Novos numero
[5] Sair do programa''')
    operação = (int(input('ESCOLHA A OPÇÂO: ')))
    if operação == 1:
        soma =  var1 + var2
        print('O valor da soma é {}'.format(soma))
    elif operação == 2:
        div = var1 / var2
        print('O valor da divisão é {}'.format(div))

    c = c + 1
print('Fim')