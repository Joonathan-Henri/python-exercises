num1 = 1
soma =0
acumlador = 0
negativos_digitados =0
print('Programa para somar')
while num1!=0:
    num1 = int(input('Digite um valor: '))
    if num1==0:
        break
    elif num1 <0:
        print('Digite um valor positivo!')
        negativos_digitados +=1
        continue
    soma +=num1
    acumlador +=1
print(f'Soma dos valores digitados:{soma}\nQuantidade de valores digitados:{acumlador}\nO Usuario digitou {negativos_digitados} numeros negativos')

