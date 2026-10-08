aumento = 0
continuar = ''
while continuar !='n':
    salario = float(input('Digite o salario do colaborador: '))

    if salario == 280:
     aumento = salario * 0.20
     salario_final = aumento + salario
     print(
        f'O seu salário era de: {salario}\nVoce recebeu um aumento de 20%\nvalor do aumento R${aumento}\nSalario final R${salario_final}\n')
     
    elif salario >= 280 and salario <= 700:
     aumento = salario * 0.15
     salario_final = aumento + salario
     print(
        f'O seu salário era de: {salario}\nVoce recebeu um aumento de 15%\nvalor do aumento R${aumento}\nSalario final R${salario_final}')
    elif salario >= 700 and salario <= 1500:
     aumento = salario * 0.10
     salario_final = aumento + salario
     print(
        f'O seu salário era de: {salario}\nVoce recebeu um aumento de 10%\nvalor do aumento R${aumento}\nSalario final R${salario_final}')
      
    elif salario >= 1500:
     aumento = salario * 0.5
     salario_final = aumento + salario
     print(
        f'O seu salário era de: {salario}\nVoce recebeu um aumento de 5%\nvalor do aumento R${aumento}\nSalario final R${salario_final}')
     
    else:  
     print('Sem aumento de salario')

    continuar = input('Voce deseja continuar? Digite S ou N ')   

def calcular_aumento(salario):
    if salario <= 280:
        percentual = 0.20
    elif salario <= 700:
        percentual = 0.15
    elif salario <= 1500:
        percentual = 0.10
    else:
        percentual = 0.05

    aumento = salario * percentual
    salario_final = salario + aumento

    return percentual, aumento, salario_final
