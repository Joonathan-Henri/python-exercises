from os import system
system('cls')

print('Loja Quase dois - Tabela de Preços')
for i in range(1, 81):
    print(f'{i:2d} - R$ {(i * 1.99):6.2f}')
    #para alinhamento dos valores a direitas :2d
    #para alinhamento dos valores em reais :6.2f, margem de 6 e duas casas decimais.
