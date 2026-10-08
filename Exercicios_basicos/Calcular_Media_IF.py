n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 9:
    print('Paranbéns, você tirou uma nota SS. Aprovado!', media)
elif media >= 7:
    print('Parabéns, você tirou uma nota S. Aprovado!', media)
elif media >= 5:
    print('Parabéns, você tirou uma nota M. Aprovado!', media)
else:
    print('Foi reprovado!')
