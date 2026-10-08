from os import system
system('cls')

idade = int(input('Digite a sua idade: '))

"""if idade< 18:
    print('Você é menor de idade')
elif idade >=18 and idade < 60:
    print('Você é adulto')
else:
    print('Você é idoso')
"""

if idade< 18:
    print('Você é menor de idade')
elif 18 <= idade < 60:
    print('Você é adulto')
else:
    print('Você é idoso')