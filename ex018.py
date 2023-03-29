"""
Faça um progama que leia um ângulo qualquer e mostre
na tela o valor do seno cosseno e tangente desse ãngulo
"""
import math
an = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tang = math.tan(math.radians(an))
print('O ângulo{} tem o SENO de {:.2f} o COSSENO de {:.2f} e a TANGENTE {:.2f}'.format(an, seno, cosseno, tang))
