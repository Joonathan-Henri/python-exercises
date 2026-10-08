from os import system
system('cls')

numbers = []
for i in range(1,11):
    numbers.append(float(input('Informe um número: ')))

numbers.reverse()
print(numbers)

'''
ou print(numbers[::-1])
'''