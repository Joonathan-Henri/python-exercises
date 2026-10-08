usuario = 'admin'
senha = 1234
while usuario == 'admin':
    usuario = str(input('Digite o nome de úsario para realizar o login: '))
    senha = int(input('Digite a senha: '))
    if usuario == 'admin' and senha == 1234:
        print('Acesso permitido!')
        break
    else:
        print('Acesso negado!')
