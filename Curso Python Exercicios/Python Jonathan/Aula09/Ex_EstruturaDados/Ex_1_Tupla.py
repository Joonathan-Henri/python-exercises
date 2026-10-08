from os import system
system('cls')

number = [] 
for i in range(0, 5): 
    number.append(int(input('Informe um número: '))) 

# Converte a lista para tupla e imprime
print(tuple(number))