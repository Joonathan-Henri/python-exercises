from os import system
system('cls')

#calcular a média das idades até que seja digitado 1000

idade = 0
soma = 0
qtd = 0

while idade != 1000:
    idade = int(input(f'Digite a idade  {qtd + 1}: '))
    if idade != 1000:
        soma += idade #soma = soma + idade
        qtd += 1 #qtd = qtd + 1
if qtd == 0:
    print('Não foi digitada alguma.')
else:
    media = soma / qtd
    print(f'A média das {qtd} idades é: {media:.2f}.')