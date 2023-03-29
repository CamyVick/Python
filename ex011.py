"""
Faça um programa que leia a largura e a altura de
uma parede em metros, calcule a sua área e
a quantidade de tinta necessária para pintá - la, sabendo
que cada litro de tinta pinta uma área de 2 metros
quadrados.
"""
alt = float(input('Qual é a altura da parede? '))
lar = float(input('Qual é a largura da parede? '))
ar = alt * lar
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(alt, lar, ar))
tin = ar / 2
print('Para pintar essa parede serão necessarios {}l de tinta'.format(tin))