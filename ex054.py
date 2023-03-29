'''
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
cont = 0
cont1 = 0
for c in range(1,8):
    a = int(input('Em que ano a {}° pessoa nasceu: '.format(c)))
    b = date.today().year
    ano = b - a
    if ano <= 21:
        cont += 1
    else:
        cont1 += 1
print('{} pessoas ainda são menores de idade\nE {} já são maiores de idade'.format(cont, cont1))
