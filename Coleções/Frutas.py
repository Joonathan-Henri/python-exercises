# As coleções podem guardar diversos valores e são mutáveis, e são delcaradas usando chaves []

# Declarando a lista com alguns dados
frutas = ['Banana', 'Maçã', 'Uva']

# Altera o valor armazenado na posição 1 da lista
frutas[1] = 'Abacaxi'

# Insere um dado ao final da coleção
frutas.append('Morango')

# Insere um valor em uma posição específica da lista
frutas.insert(1, 'Kiwi')

# Remove um valor da coleção
frutas.remove('Abacaxi')

# Verifica se o valor 'Uva' está presente na lista
if 'Uva' in frutas:
    print('Tem Uva nas frutas!')

print(frutas)

#Tuplas também podem guardar diversos valores, porem são valores imutáveis e São delcaradas utilizando parenteses ()

# Cria uma tupla chamada 'cores' com três valores
cores = ('Vermelho', 'verde', 'azul')
# Exibe o conteúdo da tupla na tela
print(cores)


# Dicionários armazenam dados no formato chave: valor.
# São muito utilizados para representar informações organizadas,
# como dados de usuários, produtos, configurações e cadastros.

# Cria um dicionário com informações de uma pessoa
pessoa = {
    'nome': 'Jonathan',
    'idade': 22,
    'cidade': 'São Paulo'
}

# Exibe todo o dicionário
print(pessoa)

# Exibe o valor associado à chave 'nome'
print(pessoa['nome'])

# Adiciona uma nova chave e seu valor
pessoa['profissao'] = 'Programador'

# Altera o valor da chave 'idade'
pessoa['idade'] = 26

# Verifica se a chave 'cidade' existe no dicionário
if 'cidade' in pessoa:
    print('A chave cidade existe!')

# Exibe todas as chaves do dicionário
print(pessoa.keys())

# Exibe todos os valores do dicionário
print(pessoa.values())

# Exibe todos os pares chave-valor
print(pessoa.items())

# Obtém um valor de forma segura
# Se a chave não existir, retorna o valor padrão informado
print(pessoa.get('telefone', 'Não informado'))

# Remove uma chave específica
pessoa.pop('cidade')

# Exibe o dicionário após as alterações
print(pessoa)