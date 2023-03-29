"""
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para
viagens de até 200Km e R$0,45 parta viagens mais longas.
"""
print('*-*' * 20)
p = str(input('Olá qual é o seu nome? ')).title()
v = str(input('Olá {} é um prazer ajudar em sua viagem!\nQual é o seu destino? '.format(p))).title()
v1 = float(input('Qual é a distancia em Km ? '))
"""if v1 <= 200:
    cal = v1 * 0.50
    print('O calculo da sua viagem para {} de {}km foi de R${:.2f}'.format(v, v1, cal))
else:
    cal2 = v1 * 0.45"""
cal = v1 * 0.50 if v1<= 200 else v1 * 0.45
print('O calculo da sua viagem para {} de {}km foi de R${:.2f}'.format(v, v1, cal))