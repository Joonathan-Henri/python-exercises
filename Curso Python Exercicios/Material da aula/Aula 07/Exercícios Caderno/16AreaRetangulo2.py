from os import system
system('cls')

# neste exemplo iremos usar a biblioteca do sistema operacional para limpar o terminal
print('Vamos calcular a area de um retangulo')
lado1 = input('Informe o primeiro lado: ')
lado2 = input('Informe o segundo lado: ')
# o metódo isnumeric valida se uma variável é um numero inteiro 
print('Lado1 é numerico?' , lado1.isnumeric())
print('Lado2 é numerico?' , lado2.isdecimal())
area = float(lado1) * float(lado2)
print('A area do quadrado é: {:.2f} ' . format(area))

#print(f'A area do quadrado é: {area:.2f}')

