altura = float(input('Digite a sua altura utilizando.'))
peso = float(input('Dígite o seu peso utilizando.'))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Você está abaixo do Peso: {imc: .2f}')
elif 20 <= imc < 25:
    print(f'Peso Ideal {imc: .2f}')
elif imc >= 25:
    print(f'Acima do Peso {imc: .2f}')
