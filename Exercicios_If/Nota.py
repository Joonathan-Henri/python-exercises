nota1 = int(input('Digite a primeira nota '))
nota2 = int(input('Digite a segunda nota '))

media = (nota1 + nota2)/2

if media < 7:
    print(f'Aprovado, a sua media foi {media}')
elif media < 10:
    print(f'Aprovado com distincão, a media foi: {media}')
else:
    print(f'Reprovado, a sua media foi {media}')
