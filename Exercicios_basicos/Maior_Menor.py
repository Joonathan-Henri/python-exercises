num1 = int(input('Digite um valor: '))
menor = num1
maior = num1
while True:
    num1 = int(input('Digite um valor: '))
    if num1 == 0:
        break
    if num1 > maior:
        maior = num1
        print(f'O valor digitado é maior{maior}')
    elif num1 < menor:
        menor = num1
        print(f'O valor digitado é menor{menor}')
