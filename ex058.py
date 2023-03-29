from random import randint
from time import sleep

n = randint(0,10) #randint- faz o computador "PENSAR"
print("-=-" * 20)
print('Vamos jogar um jogo')
print("-=-" * 20)
num = int(input('Escolha um numero entre 0 e 10 : '))
print('PROCESSANDO ... ')
sleep(3)
print("-=-" * 20)
while num != n:
    print('Ainda não foi mais uma vez')
    num = int(input(''))
print('Parabens o número sorteado {} '.format(n))