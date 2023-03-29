"""
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro
 entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep

n = randint(0,5) #randint- faz o computador "PENSAR"
print("-=-" * 20)
print('Vamos jogar um jogo')
print("-=-" * 20)
num = int(input('Escolha um numero entre 0 e 5 : '))
print('PROCESSANDO ... ')
sleep(3)
print("-=-" * 20)
if num == n:
    print('Parabéns o número escolhido foi {} também'.format(n))
else:
    print('Não foi dessa vez :( ... o numero sorteado foi {}'.format(n))
