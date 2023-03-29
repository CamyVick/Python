"""
Exercício Python 35: Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
print('=*=' * 20)
r1 = float(input('O primeiro segmento: '))
print('=*=' * 20)
r2 = float(input('O segundo segmento: '))
print('=*=' * 20)
r3 = float(input('O terceiro segmento: '))
print('=*=' * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM formar um triângulo')
else:
    print('Os segmentos NÂO PODEM formar um triângulo')
