from os import system
system('cls')

num1 = int(input('Digite um número: '))

if num1 > 0:
    if(num1 % 2 ) ==0:  # % pegará o resto da divisão
        print('O número digitado é Par')
    else:
        print('O número digitado é Impar')
else:
    print('O número digitado é igual ou menor que zero')

    
