idade = int(input('Digite a sua idade:'))
carteira = str(input('Você possui carteira de habilitação? ')).strip().lower()

if idade >= 18 and carteira == 'sim':
    print('você pode dirigir')
else:
    print('Você não pode dirigir')
