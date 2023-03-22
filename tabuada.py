
t = int(input('DIGITE O NUMERO DO QUAL VC DESEJA A TABUADA: '))
for c in range(0, 11):
    tabu = (c * t)
    print('{}x{} = {}'.format(t, c, tabu))
