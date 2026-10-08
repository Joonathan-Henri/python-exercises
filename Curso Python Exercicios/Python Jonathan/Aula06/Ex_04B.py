from os import system
system('cls')

#populações e txas iniciais

pop_A = 80000
pop_B = 200000
anos = 0

#condições para o crescimento dos países
while pop_A  <= pop_B:
    pop_A += pop_A * 0.03 #Aumento de 3%
    pop_B += pop_B * 0.015 #Aumento de 1.5%
    anos += 1 #Conta a cada ano e acrescenta

print(f'Serão necessários {anos} anos para o país A igualar ou ultrapassar o país B.')
print(f'População final do páis A: {pop_A:.0f} habitantes')
print(f'População final do páis B: {pop_B:.0f} habitantes')