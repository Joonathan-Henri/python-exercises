from os import system, name
system('cls') 


número = int(input('Informe um número: '))
# operador % restorna o restante de uma divisão
resultado = int(número % 2)
print('Se o resultado for 0 é par e se for 1 é impar, o resultado é:', resultado)
input('Ops, assim ficou ruim... assim fica melhor, digite novamente o número: ')

# if é usado para tomada de decisão
# comparação de igualdade no if sempre com ==
if resultado == 0:
    resultado = 'O número é par!'
else:
    resultado = 'O número é impar!'
print(resultado)
