from os import system
system('cls')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) /2

if media >= 10:
    print(f'A sua média é {media}, APROVADO COM DISTINÇÃO!')

elif media >= 7:
    print(f'A sua média é {media}, APROVADO!')
else:
    print(f'A sua média é {media}, REPROVADO!')