"""
Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite
"""
vel = float(input('Em quantos Km/h o seu carro estava ? '))
if vel <= 80:
    print('O seu carro está na velocidade padrão S2')
else:
    c = (vel - 80) * 7
    print('Você ultrapassou o limite de 80 Km/h e será multado em R${:.2f} '.format(c))