import random
import colorama
from colorama import Fore, Style

num =-1
acertos =0
erros=0
tentativas = 0
porcentagem = 0
historico = []

#Loop para verificar a quantidade de tentativas e se o numero digitado não e zero para fechar o programa
while num !=0 and tentativas <10:
    numero_alea =random.randint(1,10)
    tentativas +=1
    tentativas_rest = 10 - tentativas

    porcentagem = (acertos / tentativas) *100 #cacula a porcentagem de acertos após as 10 tentativas
    num = int(input(Fore.WHITE +'Digite um numero entre 1 e 10: '))      
    historico.sort()
    historico_ordenado = sorted(historico)
    historico.append(num) #armazena um valor a cada roda em uma lista
    if num == numero_alea: #verifica se o numero digitado pelo usuario é igual ao gerado
        acertos += 1
        print(f'Parabéns, voce acertou!\nRestam {tentativas_rest} tentativas')
    else:
        erros +=1
        print(f'Voce errou!\nRestam {tentativas_rest} tentativas')
if porcentagem >=80:
    print(Fore.BLUE+f'Voce é um excelente jogador! Porcentagem de de acertos {porcentagem}%')
elif porcentagem >=50:
    print(Fore.LIGHTYELLOW_EX+f'Voce é um jogador mediano! Porcentagem de acertos {porcentagem}%')
elif porcentagem >=10 or porcentagem <=40:
    print(Fore.RED+f'Voce é um jogador ruim! Porcentagem de acertos {porcentagem}%')
print(Fore.GREEN +f'Você acertou {acertos}\nVocë errou: {erros}\nEsses foram os numeros {historico_ordenado}')






#futura funcao
# dificuldade = input('Digite a dificuldade desejada: facil, médio ou dificil? ')
# if dificuldade == 'facil':
#         numero_alea =random.randint(1,10) #gerador de numeros aleatorios
# elif dificuldade == 'medio':
#         numero_alea =random.randint(1,30) #gerador de numeros aleatorios
# elif dificuldade == 'dificil':
#         numero_alea =random.randint(1,50) #gerador de numeros aleatorios
     

 