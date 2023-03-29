'''
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

soma = 0 # Ele acumula ex: 1+2+3+4+5= 15
cont = 0 # Ele conta ex: 1+1+1+1+1= 5
for c in range(1,501,2):
    if c % 3 == 0:
        cont += 1 
        soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))