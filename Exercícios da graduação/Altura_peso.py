altura = float(input('Dígite a sua altura: '))
sexo = (input('Selecione o Sexo mulher ou homem: ')).lower()


homem = (72.7 * altura) - 58.0
mulher = (62.1 * altura) - 44.7

if sexo == 'homem':
    print(f'O seu peso ideal é: {homem: .2f}')
elif sexo == 'mulher':
    print(f'O seu peso ideal é {mulher: .2f}')
else:
    print('Erro! Dígite apenas homem ou mulher')
