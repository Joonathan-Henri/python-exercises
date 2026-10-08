from random import randint
numero1 = int(input('Digite o valor para comparar: '))
numero2 = randint(1, 5)

if numero1 == numero2:
    print('Você acertou o valor!: ', numero2)
else:
    print('Você errou valor, tente novamente: ', numero2)
