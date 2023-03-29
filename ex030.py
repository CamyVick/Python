"""
Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
from time import sleep
n = int(input('Digite um numero e eu vou adivinha se é ímpar ou par: '))
n1 = n % 2
print('TÔ TE FAZENDO DE BES, DIGO "PROCESSADO"...')
sleep(3)
if n1 == 0:
    print('É PAR CARALHO')
else:
    print('É ÍMPAR ZÉ ')