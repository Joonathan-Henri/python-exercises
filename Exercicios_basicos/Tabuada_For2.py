n1 = int(input('Digite um valor para Calcular a Tabuada: '))
div = 0
cont_impar = 0
cont_par = 0
for i in range(1, 11):
    div = n1 * i
    impar = div % 2 == 0
    impares = impar
    if impar:
        cont_par += 1
        print(f'{n1} X {i} = {div} valor é par')
    else:
        print(f'{n1} X {i} = {div} valor é ímpar')
        cont_impar += 1
print(
    f'Foram gerados {cont_par} números pares\nForam gerados {cont_impar} números ímpares')
