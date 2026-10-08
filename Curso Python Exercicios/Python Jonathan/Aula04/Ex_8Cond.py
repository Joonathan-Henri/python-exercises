from os import system
system('cls')


preco1 = float(input('Digite o valor de produto 1: '))
preco2 = float(input('Digite o valor de produto 2: '))
preco3 = float(input('Digite o valor de produto 3: '))


if preco1 == preco2 and preco1 == preco3:
    print('Compre o produto 1, pois todos tem o mesmo preço')
elif preco1 < preco2 and preco1 < preco3:
    print('Compre o produto 1!')
elif preco2 < preco3:
    print('Compre o produto 2!')
else:
    print('Compre o produto 3')
