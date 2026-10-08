
nomes = []
imcs = []
continuar = 's'
while continuar!= 'n':
    nome = input('Digite o seu nome: ')
    nomes.append(nome)
    altura = float(input('Digite a sua altura:  '))
    peso = int(input('Digite o seu peso: '))
    imc = 0
    imc = peso / (altura **2)
    imcs.append(imc)
    if imc <18.5:
       print(f'iMC: {imc}, Abaixo do Peso')
    elif imc >18.5 and imc <24.9:
       print(f"IMC: {imc}, Peso Normal")
    elif imc >25 and imc <29.9:
       print(f'IMC: {imc}, Sobrepeso')
    elif imc >30 and imc<34.9:
       print(F'IMC: {imc}, Obesidade grau I')
    elif imc >35 and imc < 39.9:
       print(f'IMC: {imc}, Obesidade grau II')
    else:
       print(f'IMC: {imc}, Obesidade grau III')
    continuar = input('Vocë deseja continuar s/n?')

print(f'Total de participantes: {len(nomes)}\n')
for i in range(len(nomes)):
   print(f'Participante {nomes[i]} IMCS:{imcs[i]:.2f}', max(imcs))
   
            


