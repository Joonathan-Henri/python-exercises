turno = input(
    'Digite o turno que voce estuda  Peça para digitar M-matutino ou V-Vespertino ou N- Noturno ')

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor invalido!')
