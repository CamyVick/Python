"""
Exercício Python 34: Escreva um programa que pergunte o
salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""
nome = str(input('Qual o seu nome? ')).title()
s1 = float(input('Olá {} Qual é o seu salário ? '.format(nome)))
# Porcentagem = Valor + ( Valor * 10 / 100)
if s1 >=1250:
    c = s1 + (s1 * 10/100)
    print('O valor do seu salario com os 10% de aumento foi R${:.2f}'.format(c))
else:
    c2 = s1 + (s1 * 15 / 100)
    print('O valor do seu salario com os 15% de aumento foi R${:.2f}'.format(c2))
