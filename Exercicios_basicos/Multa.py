velocidade = float(input('Dígite a velocidade registrada: '))

multa = (velocidade - 60) * 10

if 61 <= velocidade <= 80:
    print(f'Você recebeu uma multa leve no valor de: R${multa: .2f}')
elif 81 <= velocidade < 100:
    print(f'Você recebeu uma multa grava no valor de: R${multa: .2f} ')
elif velocidade >= 100:
    print(f'Você recebeu uma multa gravíssima no valor de: R${multa: .2f}')
elif velocidade <= 30:
    print('Você está abaixo da velocidade da via, aumente a Velocidade!')
else:
    print('Você está dentro da velocidade da via, sem multa')
