from os import system
system('cls')

notas = []

for i in range(0,4):
    notas.append(float(input('Informe uma nota: ')))

soma = 0.0
print('\nNotas Digitadas: ')
for i in range(0,4):
    print(f'Nota {i+1}: {notas[i]:5.2f}')
    soma += notas[i]

print(f'Média das notas: {(soma / 4.0):5.2f}')


