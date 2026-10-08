from os import system
system('cls')

altura = float(input('Digite sua altura: '))
sexo = input('Qual seu sexo (F) ou (M): ')

if (sexo == 'M'):
    peso = (72.7 * altura) - 58
else:
     peso = (62.1 * altura) - 44.7
print(f'Seu peso ideal é: {peso:.2f}')

