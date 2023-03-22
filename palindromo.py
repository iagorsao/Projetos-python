frase = str(input(' DIGITE UMA FRASE: ')).strip().upper()
palavras = frase.split() #split vai separar a frase
junto = ''.join(palavras) #vai mostrar o split sem espaços
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} é {}'.format(junto, inverso))
print(inverso)
if inverso == junto:
    print('TEMOS UM PALINDROMO')
else:
    ('A FRASE NAO E UM PALINDROMO')