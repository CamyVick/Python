"""
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento.
"""
sal = float(input('Quanto você ganha? '))
aju = sal+(sal*15/100)
print('Com o reajuste o seu salario de R$ {:.2f} passou a ser R$ {:.2f}'.format(sal, aju))