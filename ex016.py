"""
Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela a sua porção inteira
"""
# EX.
# Digite um número : 6.127
# O número 6.127 tem a parte inteira 6
import math
from math import floor,trunc
n = float(input("Digite um número: "))
i2 = floor(n)
print("O valor inteiro de {} é {}".format(n, i2))
print("A porção inteira de {} é {}".format(n, math.trunc(n)))
print("O tanto inteiro de {} é {}".format(n, int(n)))
