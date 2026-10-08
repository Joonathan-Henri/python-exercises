a = float(input('Dígite um valor para o lado A: '))
b = float(input('Dígite um valor para o lado B: '))
c = float(input('Dígite um valor para o lado C: '))

if a < b + c and b < a + c and c < a + b:
    print('É possíovel formar um triângulo')
else:
    print('É impossível formar um triângulo')
