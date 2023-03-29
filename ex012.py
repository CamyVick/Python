"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5 % de desconto.
"""

pro = float(input('Qua o valor do seu produto? '))
p = pro - (pro * 5 / 100)
print('O valor do seu produto é de R${:.2f}. Coma promoção de 5% o produto ficou por R$ {:.2f}.'.format(pro, p))
# ---> A porcetagem equivale ao valor, vezes a porcentagem divido por 100
# ---> valor * porcetagem / 100
