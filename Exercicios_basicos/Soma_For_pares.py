soma = 0
for i in range(1, 7):
    num1 = int(input('Digite um valor para calcular os impares: '))
    if num1 % 2 == 1:
        soma += num1
    else:
        print('Nenhum valor impar foi digitado')
print(f'As somas dos valores {soma}')
