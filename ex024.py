"""
Exercício Python 24: Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome “SANTO”.
"""
cid = str(input('Qual cidade você nasceu ? ')).strip()
print(cid[0:5].upper() == 'SANTO')