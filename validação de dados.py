sexo = str(input('DIGITE SEU SEXO: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('DADOS INVALIDOS, POR FAVOR DIGITE SEU SEXO: ')).strip().upper()[0]
print('OS DADOS FORAM SALVOS COM SUCESSO ')
