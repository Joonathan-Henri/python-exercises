from os import system
system('cls')

import math

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o primeiro número: '))
num3 = float(input('Digite o número real: '))

produto = (2 * num1) * (num2 / 2)
soma = (3 * num1) + num3
cubo = math.pow(num3,3)

print(f'O produto do dobro do primeiro com a metade do segundo é {produto}\nA soma do triplo do primeiro com o terceiro é {soma}\nO terceiro ao cubo é {cubo:.2f}')

