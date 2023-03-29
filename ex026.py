"""
Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição
ela aparece a primeira vez e em que posição ela aparece a última vez.
"""
n = str(input('Digite uma frase ')).lower().strip()
print('A letra A aparece {} vezes na frase'.format(n.count('a')))
print('A letra A aperece na primeira vez na posição {}'.format(n.find('a')+1))
print('A letra A aparece pela ultima vez na posição {}'.format(n.rfind('a')+1))