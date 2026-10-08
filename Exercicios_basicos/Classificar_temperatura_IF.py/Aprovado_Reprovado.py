nota = 0
divisao = 0
soma = 0
for i in range(1, 5):
    nota = float(input('Digite a nota: '))
    soma = soma + nota
divisao = soma / 4
if divisao >= 7:

    print(f'Parabéns! Você foi aprovado com uma nota de {divisao}')
elif divisao >= 5:
    print(f'Recuperação! Você está de recuperação por ter tirado {divisao}'
          )
else:
    print(f'Você foi reprovado por tirar {divisao}')
