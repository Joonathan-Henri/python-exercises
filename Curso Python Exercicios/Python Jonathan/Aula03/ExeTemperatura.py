from os import system
system('cls')

temperatura = int(input('Digite a temperatura: '))

if temperatura <= 10:
    print('Está muito frio')
elif temperatura <= 20:
    print('Está fresco')
else:
    print('Está quente')
