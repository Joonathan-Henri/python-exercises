from os import system, name
system('cls') if(name == 'nt') else system('clear')
#são números naturais maiores do que 1 que possuem apenas dois divisores distintos: o número 1 e eles mesmos
#2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89....

numero = int(input("Digite um número inteiro: "))
i = 2
divisor = 0
tipo = 'O número deve ser maior que 2'
# usaremos o while para criar o loop
while i < numero:
    tipo = 'O número é PRIMO'
    x = numero % i
    if x == 0:
        divisor = i
        tipo = 'O número não é primo'
# comando break finaliza um loop
    break
i = i + 1
# observe que aqui usamos a função f e o nome da variável dentro das {} em vez do comando format
print(tipo)
print(f'O menor divisor é: {divisor}' if divisor > 0 else '')
