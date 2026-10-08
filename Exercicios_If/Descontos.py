valor_final = 0

num = int(input('Digite o valor do produto para calcular o desconto: '))
if num >100:
    valor_final = num * (1 - 10/100)
    print(f'Voce recebeu um desconto de 10%\nValor final do produto: R${valor_final}')
elif num <=100:
    valor_final = num * (1 - 5/100)
    print(f'Voce recebeu um desconto de 5%\nValor final do produto: R${valor_final}')
    