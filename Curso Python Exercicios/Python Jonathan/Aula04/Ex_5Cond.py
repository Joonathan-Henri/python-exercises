from os import system
system('cls')

num = int(input('Digite o primeiro número: '))

if num > 0:
    print('O número digitado é posítivo')
elif num < 0:
    print('O número digitado é negativo')
else:
    print('O número digitado é igual aZero')