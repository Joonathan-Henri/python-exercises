senha = 'jonathan'
tentativas = 0

for i in range(1,4):
    senha = str(input('Digite a senha para acessar: ')).lower()
    if senha =='jonathan':
        print('Acesso permitido')
        break
else:
    print('A quantidade de tentivas ultrapassou 3 vezes')
   
       