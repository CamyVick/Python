'''
Crie um programa que faça o computador jogar Jokenpô com você
'''
from time import sleep
import random
n = int(random.randint(1,3))
b = print('**************Vamos jogar um jogo**************')
a = int(input('''Escolha uma das opções abaixo:
1 - Pedra
2 - Tesoura
3 - Papel
\n
'''))
print('PEDRA!')
sleep(1)
print('PAPEL!')
sleep(1)
print('TESOURA!')
sleep(1) 

if n == 1 and a == 1:
    print('**************EMPATE**************')
    print('O computador escolheu PEDRA e você PEDRA')
elif n == 1 and a == 2:
    print('**************PERDEU**************')
    print('O computador escolheu PEDRA e você TESOURA')
elif n == 1 and a == 3:
    print('**************GANHOU**************')
    print('O computador escolheu PEDRA e você PAPEL')

elif n == 2 and a == 2:
    print('**************EMPATE**************')
    print('O computador escolheu TESOURA e você TESOURA')
elif n == 2 and a == 1:
    print('**************GANHOU**************')
    print('O computador escolheu TESOURA e você PEDRA ')
elif n == 2 and a == 3:
    print('**************PERDEU**************')
    print('O computador escolheu TESOURA e você PAPEL')

elif n == 3 and a == 3:
    print('**************EMPATE**************')
    print('O computador escolheu PAPEL e você PAPEL')
elif n == 3 and a == 2:
    print('**************GANHOU**************')
    print('O computador escolheu PAPEL e você TESOURA')
elif n == 3 and a == 1:
    print('**************PERDEU**************')
    print('O computador escolheu PAPEL e você PEDRA ')

else:
    print('Comando inexistete')

