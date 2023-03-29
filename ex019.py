"""
Um professor quer sortear um dos seus 4 alunos
para apagar o quadro. Faça um programa que ajude
ele, lendo os nomes deles e escrevendo o nome escolhidos
"""
from random import choice

n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digete o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
list = [n1, n2, n3, n4]
escolhido = choice(list)
print('O escolhido foi {}'.format(escolhido))