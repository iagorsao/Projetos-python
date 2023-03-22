import random
from time import sleep
giro = 0
print('-=' * 20 )
print('VAMOS JOGAR')
print('-=' * 20)
numero = random.randint(0, 10)
print(numero)
sleep(2)
acertou = False

while not acertou :
    adv = int(input('TENTE ADIVINHAR O NUMERO: '))
    if adv == numero:
        acertou = True
    elif adv < numero:
        print('Mais')
    elif adv > numero:
        print('Menos')
    giro = giro + 1

print('Depois de {} tentativas voce acertou '.format(giro))