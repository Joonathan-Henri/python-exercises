from os import system
system('cls')

nota = float(input('Digite a nota do aluno: '))

if nota >= 9:
    print('Execelente, você tirou uma A')
elif nota >= 7:
    print('Bom trabalho, você tirou um B')
elif nota >=5:
    print('Você passou, mas precisa melhorar. Sua nota é C')
else:
    print('Reprovado.')

