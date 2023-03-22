km = float(input('Quantos KM foram Rodados? '))
dias = int(input('Quantos dias foram utilizados? '))
cdc = 60*dias
ckc = 0.15*km
ctc = cdc+ckc
print('O valor total ficara {}'.format(ctc))