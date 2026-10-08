from os import system
system('cls')

numeros = []
pares = []
impares = []

for i in range(0, 8):
    numero = int(input('Informe um número: '))
    numeros.append(numero)
    if (numero % 2) == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('Números: ', numeros)
print('Pares: ', pares)
print('Impares: ', impares)


