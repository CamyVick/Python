"""
Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import date
ano = int(input('Qual é o ano que você quer analizar ? '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or 400 == 0:            # Tem que ser divisivél por 4 e também não pode ser dividido por 100 !-= ,ou então o ano ser divisivél por 400
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))