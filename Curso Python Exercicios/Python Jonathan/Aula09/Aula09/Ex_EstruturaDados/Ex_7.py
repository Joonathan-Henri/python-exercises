from os import system
system('cls')

numeros = []
for i in range(0, 5):
    numeros.append(int(input('Informe um número inteiro: ')))

soma = 0
multiplicacao = 1
for i in numeros:
    soma += i
    multiplicacao *= i

print(numeros)
print(f'Soma dos números: {soma}')
print(f'Multiplicação dos números: {multiplicacao}')    