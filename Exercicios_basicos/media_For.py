soma = 0
for i in range(1, 5):
    num1 = float(input('Digite a nota para calcular a média: '))
    soma += num1
    div = soma / 4
    if (div >= 9):
        print(f'Parabéns!!, você tirou uma nota A+ {div}')
    elif (div >= 7):
        print(f'Parabéns!, você tirou uma nota B {div}')
    elif (div >= 5):
        print(f'Parabens, você tirou uma nota C {div}')
else:
    print('Reprovado! Nota abaixo do aceitável')
