from os import system
system('cls')

print('Vamos calcular a area de um retangulo')
lado1 = input('Informe o primeiro lado: ')
lado2 = input('Informe o segundo lado: ')

# Substitui a vírgula por ponto (caso o usuário digite no padrão brasileiro)
lado1 = lado1.replace(',', '.')
lado2 = lado2.replace(',', '.')

try:
    # Tenta converter os dois lados para números decimais
    area = float(lado1) * float(lado2)
    
    print('Lado1 é um número válido? True')
    print('Lado2 é um número válido? True')
    print(f'A area do retângulo é: {area:.2f}')

except ValueError:
    # Se o usuário digitou letras ou símbolos inválidos, cai aqui
    print('\nErro: Um ou ambos os lados informados não são números válidos!')