from os import system, name
system('cls') if(name == 'nt') else system('clear')

print('*** Tabuada Simples ***')

multiplicador = int(input('Informe o multiplicador '))
# para criar o loop usaremos a função for e range
i = 1
for i in range(1,11):
    print('{} * {} = {}' . format(multiplicador, i, i*multiplicador))
