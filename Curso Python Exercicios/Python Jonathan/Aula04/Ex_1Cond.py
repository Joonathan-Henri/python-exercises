from os import system
system('cls')

fruta = input('Fruta: ').lower()

if (fruta == 'banana'):
    print('O Kg da Banana é R$ 5,23')
elif (fruta == 'maça'):
    print('O Kg da Maça é R$ 12,10')
elif (fruta == 'cereja'):
    print('O Kg da Cereja é R$ 58,00')
else:
    print('Desculpe! Não temos ', fruta)