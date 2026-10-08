from os import system
system('cls')

print('Vamos calcular a raiz quadrada')
n = input('informe o número: ')

# Substitui a vírgula por ponto, caso o usuário digite no formato brasileiro
n = n.replace(',', '.')

# Verifica se o texto pode ser convertido para número
try:
    # Converte para float (aceita inteiros e decimais)
    numero_validado = float(n)
    
    # Verifica se ele é inteiro verificando se o resto da divisão por 1 é zero
    eh_inteiro = numero_validado.is_integer()
    
    print(f'O valor é um número inteiro? {eh_inteiro}')
    print(f'O valor é um número com casas decimais? {not eh_inteiro}')
    
    # Calcula a raiz quadrada
    resultado = numero_validado ** 0.5
    
    print(f'A raiz quadrada de {n} é {resultado:.2f}')

except ValueError:
    print('Erro: O valor digitado não é um número válido.')