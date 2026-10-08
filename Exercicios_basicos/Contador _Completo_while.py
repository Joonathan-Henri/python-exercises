num1 = 0
soma = 0
pares = 0
impares = 0
while True:
    num1 = int(input('Digite um valor para calcular a soma, pares e ímpares: '))
    if num1 == 0:
        break
    soma += num1
    if num1 % 2 == 1:
        impares += 1
    else:
        pares += 1
print(
    f' A soma é: {soma}\n A quantidade de impares é: {impares}\n a quantidade de pares é: {pares}')
