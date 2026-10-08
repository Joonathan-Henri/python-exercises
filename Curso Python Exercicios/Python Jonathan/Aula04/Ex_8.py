from os import system
system('cls')

f = float(input('Digite a temperatura em Faremheit: '))

c = 5 * (f - 32) / 9

print(f'A temperatura em Celsius é {c:.2f}')

