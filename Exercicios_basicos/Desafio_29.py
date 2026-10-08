vel = int(input('Digite a velocidade do carro: '))
permitido = 80

if vel > permitido:
    excesso = vel - permitido
    multa = excesso * 7
    print('Você foi multado por ultrapassar o limite de velocidade!', multa)
else:
    print('Você está dentro da velocidade permitida')
print('Fim do programa')
