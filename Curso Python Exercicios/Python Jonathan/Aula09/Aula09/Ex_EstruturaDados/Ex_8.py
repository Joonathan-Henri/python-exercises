from os import system
system('cls')

pessoas = []

for i in range(0, 5):
    pessoa = []
    pessoa.append(input(f'Informe a idade da pessoa {i + 1}: '))
    pessoa.append(input(f'Informe a altura da pessoa {i + 1}: '))
    pessoas.append(pessoa)

pessoas.reverse()
for pessoa in pessoas:
    print(f'Idade: {pessoa[0]} - Altura: {pessoa[1]}')

        