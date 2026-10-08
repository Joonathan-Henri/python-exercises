nota = 0
soma=0
for i in range(1,6):
    nota = float(input('Digite as notas para calcular a média: '))
    soma += nota
resultado = soma/ 5
print(f'Média: {resultado}')