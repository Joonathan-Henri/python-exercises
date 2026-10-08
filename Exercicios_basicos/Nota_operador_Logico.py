nota = int(input('Digite a nota: '))
presenca = int(input('Digite a porcentagem da presença: '))

if nota >= 6 and presenca >= 75:
    print('Você passou!')
else:
    print('Você foi reprovado!')
