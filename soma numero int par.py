soma = 0
cont = 0
for num in range (1,7):
   n = int(input('Digite seu numero: '))
   if n % 2 == 0:
      soma = soma + n
      cont = cont + 1
print(' vc informou {} numero pares e a soma dos numero pares é igual a {}'.format(cont, soma))


