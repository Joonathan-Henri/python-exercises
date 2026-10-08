from os import system
system('cls')

letras = []
vogais = ['A', 'E', 'I', 'O', 'U']

for i in range(0, 10):
    letras.append(input('Informe um caracter: ').upper())

totConsoantes = 0
consoante = []

for i in range(0,10):
    if letras[i] not in vogais:
        consoante.append(letras[i])
        totConsoantes += 1

print(f'Você digitou {totConsoantes} consoantes!')
print(consoante)        
