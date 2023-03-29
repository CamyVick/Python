"""
Faça um programa  que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa
"""
# Teoréma de Pitágoras a²= b²+c²
# from math import sqrt
import math
a = float(input("Digite o comprimento do cateto adjacente: "))
o = float(input("Digite o comprimento do cateto oposto: "))
# h = (a ** 2 + o ** 2) ** (1/2)
#r = sqrt(h)
hi = math.hypot(a, o)
print("A soma dos quadrados dos catetos {} e {} é igual a {:.2f}".format(a, o, hi))
# Então: 5² = 3² + 4² ⇒ 25 = 9 + 16 ⇒ 25 = 25