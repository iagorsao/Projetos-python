from time import sleep  #jogo da adivinhação
import random
n = random.randint(0, 5)
print('-=-' * 20)
m = int(input('Qual o numero gerado pelo computador? : '))
print('PROCESSANDO!!!!')
sleep(2)
print('-=-' * 20)
if n == m:
    print(' Você venceu!!!!')
else:
    print('Tente outra vez!!')
print('FIM DA PARTIDA')