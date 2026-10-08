from os import system, name
system('cls') if(name == 'nt') else system('clear')
#são números naturais maiores do que 1 que possuem apenas dois divisores distintos: o número 1 e eles mesmos
#2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89....

numero = int(input("Digite um número inteiro positivo: "))

# Números menores ou iguais a 1 não são primos
if numero <= 1:
    print(f"O número {numero} não é primo.")
else:
    # Conta quantas vezes o número foi dividido com resto zero
    divisores = 0
    
    # Testa as divisões de 1 até o próprio número
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
            
    # Se foi dividido apenas 2 vezes (por 1 e por ele mesmo), é primo
    if divisores == 2:
        print(f"O número {numero} é PRIMO!")
    else:
        print(f"O número {numero} NÃO é primo (ele tem {divisores} divisores).")