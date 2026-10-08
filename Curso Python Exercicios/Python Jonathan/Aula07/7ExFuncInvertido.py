from os import system
system('cls')

def retornaInvertido(valor):
    return valor[::-1]
#fatiamento [inicio:fim:passo], colchetes após um variável é fatiamento

numero = (input('Informe um número: '))
print(retornaInvertido(numero))