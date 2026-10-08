total = 0
media = 0
soma = 0
num1 = 0
while True:
    num1 = int(input('Digite um valor para calcular soma, media e total: '))
    if num1 == 0:
        break
    soma += num1
    total += 1
    media = (soma) / total
print(
    f'\n A soma dos valores é: {soma},\n A média dos valores é: {media} \n O total de valores digitados é: {total}')
