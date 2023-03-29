"""
Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos dólares ela pode comprar.
"""
# --->Valor do dolar 5,35
r = float(input('Quanto você tem na carteira? R$:'))
d = r / 5.35
e = r / 6.43
print(' Com valor de R${:.2f} você pode comprar US{:.2f} \n ou £{:.2f}'.format(r, d, e))
