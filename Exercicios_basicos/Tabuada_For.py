num1 = int(input('Digite um número para calcular a tabuada: '))
print('============================')
total = 0
for i in range(1, 11):
    total = num1 * i
    print(f'{num1} x {i} = {total}')
print('=============================')
