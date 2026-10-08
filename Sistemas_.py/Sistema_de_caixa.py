produtos = []
precos = []
total = 0

while True:
    #menu com as opcoes
    print('\nCaixa da loja')
    print('1 - Adicionar produto')
    print('2 - Buscar produto')
    print('3 - Finalizar')

    #Recebe o valor digitado pelo usuario e compara nos ifs
    opcao = int(input('Escolha uma opcao: '))
    #Os if fazem a comparacao logica para entrar nos menus corretos
    if opcao == 1:
       print("\n--- Adicionando produto ---")
       produto = input('Digite o nome do produto: ')
       produtos.append(produto)
       preco = float(input('Digite o valor do produto: '))
       precos.append(preco)
    elif opcao == 2:
        nome = input('Digite o nome do produto que deseja buscar')
        if nome in produtos: 
          print('Produto está no carrinho')
        else:
          print('Produto não encontrado')
    elif opcao ==3:
       break 
    #faz o soma total dos produtos    
total = sum(precos)

#faz a comparacao para verificar se tem mais de 10 itens no carrinho e aplica o desconto caso a condicao seja verdadeira
if len(produtos) >10: 
    desconto = total * 0.10
    valor_final = total - desconto
    #loop que percorre a lista para apresentar os produtos de uma forma mais clara
    for i, produto in enumerate(produtos):
     print(i +1, '-', produto)
    print(f'Desconto de 10% aplicado.\nValor sem desconto R${total}.\nValor do pedido com desconto R${valor_final:.2f}')
else:
    for i, produto in enumerate(produtos):
     print(i +1, '-', produto)
print(f'Valor total do pedido R${total}')

   


    

