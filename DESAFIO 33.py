n1 = float(input('digite um numero 1: '))
n2 = float(input('digite um numero 2: '))
n3 = float(input('digite um numero 3: '))
if n1 > n2 and n1 > n3 :
    print('{} é o maior numero'.format(n1))
if n2 > n1 and n2 > n3 :
    print('{} é o maior numero'.format(n2))
if n3 > n1 and n3 > n2:
    print('{} é o maior numero'.format(n3))
if n1 < n2 and n1 < n3 :
    print('{} é o menor numero'.format(n1))
if n2 < n1 and n2 < n3 :
    print('{} é o menor numero'.format(n2))
if n3 < n1 and n3 < n2:
    print('{} é o menor numero'.format(n3))

