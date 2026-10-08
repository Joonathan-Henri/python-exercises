from os import system
system('cls')

import random

opcoes = ['PAPEL', 'TESOURA', 'PEDRA']

escolha1 = input('Entre com: Papel, Pedra, ou Tesoura: ').upper()
escolha2 = random.choice(opcoes)

print(f'Você escolheu {escolha1}.')
print(f'O computador escolheu {escolha2}.')

if escolha1 == escolha2:
    print('Empate!')
    print('Empate!')
elif (escolha1 == 'PEDRA' and escolha2 == 'TESOURA') or (escolha1 == 'TESOURA' and escolha2 == 'PAPEL') or \
      (escolha1 == 'PAPEL' and escolha2 == 'PEDRA'):
    print('Você  Venceu!!')
else:
    print('O computador Venceu!!')