# a variável continuar controla o loop, guardando a resposta do usuário para continuar ou parar o programa
continuar = ''

#cria uma lista para receber as temperaturas
temperaturas = []

# laço de repetição que continua enquanto a variável 'continuar' for diferente de 'n'
while continuar != 'n':               
    tipo = int(input('Digite 1 para converter Celsius para Fahrenheit\nDigite 2 para converter Fahrenheit para Celsius:\nDigite 3 para converter Celsius para Kelvin:\n'
    'Digite 4 para converter Kelvin para Celsius: '))
                
    # todos os ifs e elifs verificam a opção selecionada através da variável tipo e iniciam o bloco correspondente
    # dentro de cada estrutura o .append guarda o resultado na lista e o print exibe o resultado ao usuário   

    if tipo == 1:
        celsius = float(input('Digite o valor em celsius para transformar em Fahrenheit: '))
        if celsius < -273.15:
            print('Não é possível converter um valor menor que -273.15. Digite um valor acima desse')
        else:
            fahrenheit = (9/5 * celsius) + 32
            print(f'A connversão de celsius para Fahrenheit é: {fahrenheit:.2f}°F')
            temperaturas.append(f'A connversão de celsius para Fahrenheit é: {fahrenheit:.2f}°F')
  
    elif tipo == 2:
        fahrenheit = float(input('Digite o valor em Fahrenheit para transformar em Celsius: '))
        if fahrenheit < -459.67:
            print('Não é possível converter um valor menor que -459.67. Digite um valor acima desse')
        else:
            celsius = 5/9 * (fahrenheit - 32)   
            print(f'A conversão de Fahrenheit para Celsius é: {celsius:.2f}°C')
            temperaturas.append(f'A conversão de Fahrenheit para Celsius é: {celsius:.2f}°C')

    elif tipo == 3:
        celsius = float(input('Digite o valor em Celsius para transformar em Kelvin: '))
        if celsius < -273.15:
            print('Não é possível converter um valor menor que -273.15. Digite um valor acima desse')
        else:
            kelvin = celsius + 273.15
            print(f'A conversão de Celsius para Kelvin é: {kelvin:.2f}K')
            temperaturas.append(f'A conversão de Celsius para Kelvin é: {kelvin:.2f}K')

    elif tipo == 4:
        kelvin = float(input('Digite o valor em Kelvin para transformar em Celsius: '))
        if kelvin < 0:
            print('Não é possível converter um valor menor que 0K. Digite um valor acima desse')
        else:
            celsius = kelvin - 273.15
            print(f'A conversão de Kelvin para Celsius é: {celsius:.2f}°C')
            temperaturas.append(f'A conversão de Kelvin para Celsius é: {celsius:.2f}°C')

    else: 
        print('Opcao inválida')

    # atualiza a variável continuar para que o while verifique na próxima iteração se deve continuar ou parar
    continuar = (input('Deseja continuar s/n? '))

# for percorre todos os valores guardados na lista e exibe o histórico de conversões
for i in range(len(temperaturas)):
    print(f'{temperaturas[i]}')