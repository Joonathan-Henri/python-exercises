from os import system
system('cls')

def qtDigitos(digito):
    if digito == 0:
        return 0
    return 1 + qtDigitos(int(digito/10))
#Divisão base 10 o computador somente conta os inteiros.
#ENTRADA DADOS

digito = int(input('Informe um número inteiro:'))
print(f'O número {digito} possui {qtDigitos(digito)} digitos.')