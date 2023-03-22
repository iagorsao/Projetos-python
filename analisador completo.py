somaidade = 0
maisvelho = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1,5):
    nome = str(input('Nome da {}ª pessoa : '.format(c))).strip()
    idade = int(input('Idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Digite o sexo M/F {}ª pessoa: '.format(c))).strip()
    somaidade = somaidade + idade

    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1

media =  (somaidade/c)
print('A media de todas as idades é igual a {}'.format(media))
print('O homem mais velho  tem {} anos  e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres a baixo de 20 anos'.format(totmulher20))