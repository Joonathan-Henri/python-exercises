senha = 'Gato'
usuario = ''
tenativas = 0

while (usuario != senha):
    usuario = str(input('Digite a senha: '))
    if usuario != senha:
        print('Acesso negado!')
print('Acesso permitido')
