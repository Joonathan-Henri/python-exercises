# operacao = str(input('Selecione a operação desejada: ')) teste

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segunda valor: '))

total = n1 + n2

print('\033A soma entre {} e {} vale {}\033'.format(n1, n2, total))
