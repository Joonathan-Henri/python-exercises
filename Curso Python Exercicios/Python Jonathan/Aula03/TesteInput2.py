from os import system
system('cls')

valorProd = float(input('Digite o valor do seu produto: R$'))

valorAcrecscimo = valorProd * 1.10

print(f'O valor final do produto. com acréscimo é R$ {valorAcrecscimo:.2f}')