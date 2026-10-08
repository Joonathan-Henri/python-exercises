from os import system
system('cls')

horario = int(input('Digite o horário: '))

if horario < 12:
    print('Bom dia!')
elif horario < 18:
    print('Boa tarde!')
else:
    print('Boa noite!')
