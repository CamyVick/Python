'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de 
artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from time import sleep
input('Vamos iniciar a contagem regressiva para o Ano Novo')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!!!!!!')