

print('Cálculo da folha de pagamento')
horas_trab = int(input('Digite quantas horas vocë trabalhou no mes: '))
valor_hora = float(input('Digite o valor da sua hora: '))


valor_bruto = horas_trab * valor_hora
descontos = 0
fgts = 0
sindicato = 0
salario_liquido = 0
ir=0
inss = 0

if valor_bruto >= 2500:
    sindicato = valor_bruto * 0.03
    fgts = valor_bruto * 0.11
    inss = valor_bruto * 0.10
    ir = valor_bruto * 0.05
    descontos = sindicato + inss + ir
    salario_liquido = valor_bruto - descontos
    print(f'\n Valor Bruto R${valor_bruto}\n FGTS 10%  R${fgts}\n IR 5% R${ir}\n INSS 10% R${inss}\n Sindicato 3% R${sindicato}\n Total de desconto R${descontos}\n Salário Liquido R${salario_liquido}')
elif valor_bruto >= 1500:
    sindicato = valor_bruto * 0.03
    fgts = valor_bruto * 0.11
    inss = valor_bruto * 0.10
    ir = valor_bruto * 0.05
    descontos = sindicato + inss + ir
    salario_liquido = valor_bruto - descontos
    print(f'\n Valor Bruto R${valor_bruto}\n FGTS 10%  R${fgts}\n IR 5% R${ir}\n INSS 10% R${inss}\n Sindicato 3% R${sindicato}\n Total de desconto R${descontos}\n Salário Liquido R${salario_liquido}')
elif valor_bruto >= 900:
    sindicato = valor_bruto * 0.03
    fgts = valor_bruto * 0.11
    inss = valor_bruto * 0.10
    descontos = sindicato + inss
    salario_liquido = valor_bruto - descontos
    print(f'\n Valor Bruto R${valor_bruto}\n FGTS 10%  R${inss}\n INSS 10% R${inss}\n Sindicato 3% R${sindicato}\n Total de desconto R${descontos}\n Salário Liquido R${salario_liquido}')

