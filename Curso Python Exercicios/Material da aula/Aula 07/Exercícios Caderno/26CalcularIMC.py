from os import system, name
system('cls') if(name == 'nt') else system('clear')
                                           
print('*** CALCULADORA DE IMC ***')
peso = int(input('Informe o seu peso em KG: '))
altura = float(input('Agora a sua altura em centimetros: '))/100
imc = peso / (altura * altura)

print(f"O seu IMC é de {imc:.2f}")

if imc < 18.5:
    resultado = 'Abaixo do Peso'
elif imc < 25:
    resultado = 'Peso Normal'
elif imc < 30:
    resultado = 'Sobrepeso'
elif imc < 35:
    resultado = 'Obesidade Grau I'
elif imc < 40:
    resultado = 'Obesidade Grau II'
else:
    resultado = 'Obesidade Grau III'

print(resultado)

