from os import system
system('cls')

vlhora = float(input('Qual o valor da sua hora trabalhada? '))
horas= int(input('Informe a quantidade de horas trabalhadas: '))

print(f'Seu salário este mês será{(vlhora * horas):.2f}')