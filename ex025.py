"""
Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""
n = str(input('Qual o seu nome ? ')).strip().lower()
print('Seu nome tem silva? {}'.format('silva' in n))