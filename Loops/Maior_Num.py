soma = 0
media = 0
maior =0

print('Programa para cacular maior, média e soma')
for i in range(1,6):
    num = int(input('Digite um numero inteiro: ')) 
    soma = soma + num
    media = soma / 5  
    if num > maior:
        maior = num              
print(soma, media, maior)

