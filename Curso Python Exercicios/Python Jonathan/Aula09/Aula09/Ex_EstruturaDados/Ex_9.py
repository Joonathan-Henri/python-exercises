from os import system
system('cls')

a = []
for i in range(0, 10):
    a.append(int(input('Informe um número: ')))

somaQuadrado = 0
for numero in a:
    somaQuadrado += (numero * numero)

print(f'A soma dos quadrados dos números lidos é: {somaQuadrado}')

