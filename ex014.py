'''
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''
c = float(input('Qual sua temperatura em Cº? '))
t = ((9 * c) / 5) + 32
print('A sua temperatura em graus Cº é de {} que convertido para Fahrenheit é {}'.format(c, t))
f = float(input('Qual a sua temperatura em F?'))
# ---> 9 * c / 5 -32