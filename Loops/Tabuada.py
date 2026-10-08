num1 = int(input('Digite um valor para cacular a tabuada: '))
total =0
for i in range(1,11):
    total = num1 * i
    print(f'{num1} X {i} = {total}')