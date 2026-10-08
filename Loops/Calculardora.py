soma = 0
divisao = 0
multipliacao = 0
subtracao = 0

opcao = str(input('Escolha a operacao desejada: soma, multiplicacao, divisao, subtracao: '))

for i in range(1,3):
    num = int(input('Digite um valor: '))
    if opcao == 'soma':                     
     soma += num
     print(soma)
    if opcao == 'multi':
       multipliacao = num * i
print(multipliacao)
