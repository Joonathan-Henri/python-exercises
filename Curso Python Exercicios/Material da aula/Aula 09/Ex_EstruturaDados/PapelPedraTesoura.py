from os import system
system('cls')

import random
opcoes = ['PAPEL', 'TESOURA', 'PEDRA']

escolha1 = input('Entre com: Papel, Pedra ou Tesoura: ').upper()
escolha2 = random.choice(opcoes)

print(f'VOCÊ escolheu {escolha1}.')
print(f'O COMPUTADOR escolheu {escolha2}.')

if escolha1 == escolha2:
    print('Empate!')
elif (escolha1 == 'PEDRA' and escolha2 == 'TESOURA') or (escolha1 == 'TESOURA' and escolha2 == 'PAPEL') or \
      (escolha1 == 'PAPEL' and escolha2 == 'PEDRA'):
    print('Você venceu!!!')
else:
    print('O computador venceu!!!')


        