idade = int(input('Digite a idade: '))
convite = (input('Você tem o convite?')).lower()

if idade >= 18 or convite == 'sim':
    print('Acesso liberado!')
else:
    print('Acesso negado!')
