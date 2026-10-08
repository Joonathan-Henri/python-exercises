notas = []
nomes =[]
continuar = ''

media = 0
maior = 0
menor = 0

while continuar != 'n':
    nome = input('Digite o nome do aluno: ')
    nomes.append(nome)
    nota = float(input('Digite a nota: '))
    notas.append(nota)

    continuar = input('Voce deseja continuar? s/n: ')
media = sum(notas) / len(notas)
notas.index(max(notas))
indice_maior = notas.index(max(notas))
print(nomes[indice_maior])