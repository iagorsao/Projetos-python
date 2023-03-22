print('-='*20)
print("ANALISADOR DE TRIANGULOS")
print('-='*20)
r1 = float(input('Digite o 1 comprimento da reta: '))
r2 = float(input('Digite o 2 comprimento da reta: '))
r3 = float(input('Digite o 3 comprimento da reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('as retas acimas podem formar um triangulo')
else:
    print('nao podem formar um triangulo')