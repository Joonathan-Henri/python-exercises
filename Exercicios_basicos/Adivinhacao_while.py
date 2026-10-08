import random
num1 = 0
erros = 0
acertos = 0
print('Programa de adivinhação')
while (num1 != -1):
    num1 = int(input('Digite um valor para verificar: '))
    aleatorio = random.randint(1, 10)
    if (num1 == -1):
        break
    if (num1 == aleatorio):
        print(f'Você acertou o número! {aleatorio}')
        acertos += 1
    else:
        print('Você errou!')
        erros += 1
print(f'Você acertou: {acertos} e errou: {erros}')
