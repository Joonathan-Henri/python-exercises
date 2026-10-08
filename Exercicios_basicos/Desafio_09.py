print('Programa que cálcula a tabuada')
n1 = int(input('Digite o valor para calcular a tabuada: '))

resultado = n1 * n1

for i in range(1, 11):
    resultado = n1 * i
    print(f"{n1} x {i} = {resultado}")
