'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.
'''
soma = 0
cont = 0
for c in range(1,7):
    nu = int(input('Digite o {} valor :) '.format(c)))
    if nu % 2 == 0:
        soma += nu
        cont += 1
print('A soma dos {} números pares foi: {} '.format(cont, soma))