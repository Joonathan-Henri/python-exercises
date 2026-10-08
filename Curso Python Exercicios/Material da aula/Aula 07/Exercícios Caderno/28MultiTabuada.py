from os import system, name
system('cls') if(name == 'nt') else system('clear')

print('\n*** MULTI TABUADA 1 ***\n')

for i in range(1, 11):
    print('{: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4}' . format(i, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10))
"""
O comando {: >4} é um formatador que reserva 4 espaços de texto e alinha o número à direita. Isso 
garante que as colunas fiquem perfeitamente alinhadas, mesmo quando mudamos de números com 1 dígito 
para números com 2 ou 3 dígitos.
"""

print('\n*** MULTI TABUADA 2 ***\n')
# usando um for dentro de outro
for i in range(1, 11):
    linha = '{: >4} ' . format(i)
    for ii in (range(2, 11)):
        linha+='{: >4} ' . format(ii*i)
    print(linha)
