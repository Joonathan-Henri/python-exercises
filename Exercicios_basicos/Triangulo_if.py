ladoA = 0
ladoB = 0
ladoC = 0

ladoA = float(input('Digite o valor A: '))
ladoB = float(input('Digite o valor B: '))
ladoC = float(input('Digite o valor C:'))
if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    print('Triângulo válido!')
else:
    print('Triângulo inválido!')
