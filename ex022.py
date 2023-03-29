"""
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao tod(sem considerar espaços).

– Quantas letras tem o primeiro nome.
"""

nome = str(input('Qual o seu nome completo? ')).strip()
print('Analizando seu nome...')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome) -nome.count(' ')))

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

