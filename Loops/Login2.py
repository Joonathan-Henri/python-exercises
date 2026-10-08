while True:
    usuario = input('Digite o seu nome de usuario: ')
    senha = input('Digite a sua senha: ')

    if len(senha) < 8:
        print("Senha curta demais!")
        continue
    if usuario == senha or senha == usuario:
        print('Tente novamente, a senha e o usuario não podem ser iguais')
    else:
        print('Cadastro realizado com sucesso!')
        break
    

