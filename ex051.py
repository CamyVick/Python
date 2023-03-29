'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.

'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('A razão: '))
decimo = primeiro + (10 - 1) * razao # eneximo termo de uma PA
for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end=' - ')
print('ACABOU')