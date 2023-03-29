"""
Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# Verificar menor
menor = a
if b<a and b<c:
    menor = b
if c<b and c<a :
    menor = c
# Verificando o maior
maior = a
if b>a and b>c:
    maior = b
if c>b and c>a:
    maior =c
print('O menor valor digitado foi {}'.format(menor))
print('E o maior valor digitado foi {}'.format(maior))
