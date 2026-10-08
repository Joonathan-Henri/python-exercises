from os import system
system('cls')

letra = input('Informe uma letra: ')

if ('AEIOU'.find(letra.upper()) >=0): 
    print('A letra digitada é uma vogal!')
else:
    print('A letra digitada é uma consoante!')  

'''.FIND LOCALIZA A POSIÇÃO DE UMA SUBSTRING DENTRO DE UMA STRING, 
SE NÃO ENCONTRADA RETORNA - 1 '''