'''
Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem
- O primeiro valor é maior
- O segundo valor é maior
- Não exite valor maiores os dois são iguais 
'''
valor_1 = int(input('Digite o primeior valor: '))
valor_2 = int(input('Digite o segundo valor: '))
if valor_1>valor_2:
    print('O primerio valor ({}) é o maior'.format(valor_1))
elif valor_2>valor_1:
    print('O segundo valor ({}) é o maior'.format(valor_2))
else:
    print('Não existe maior pois os dois são iguais.')