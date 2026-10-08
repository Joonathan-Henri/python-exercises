num1 = 1
negativo = 0
positivo = 0
while num1 !=0:
    num1 = int(input('Digite um numero: '))
    if num1 > 0:
     positivo += 1              
     print('numero postivo')    
    elif num1 ==0:
     break
    elif num1 <=0:
      print('Numero negativo')
      negativo +=1     
print(f'Total de numeros positivo:{positivo}\nTotal de numeros negativos:{negativo}')