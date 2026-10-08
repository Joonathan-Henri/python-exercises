desconto = 0
num1 = int(input('Digite o valor do item para calcular o desconto: '))
preco_final = 0

if num1 > 500:
    desconto = num1 * 0.15
    preco_final = num1 - desconto
    print(f'Você obteve um desconto de, preço final:{preco_final:.2f}')
elif num1 > 200:
    desconto = num1 * 0.10
    preco_final = num1 - desconto
    print(
        f'Você obteve um desconto de {desconto:.2f}, preço final:{preco_final:.2f}')
else:
    print('Sem desconto')
