from os import system
system('cls')

import json

lista = [1,2,3,4,5,6,7,8,9] #dados em python
dados_json = json.dumps(lista) #convertido para json

print(dados_json)
print(type(dados_json))