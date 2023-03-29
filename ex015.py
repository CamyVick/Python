"""
Escreva um programa que pergunte a quantidade
de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
k = float(input('Quantos km você rodou? '))
d = int(input('Por quantos dias você rodou? '))
pk = k * 0.15
pd = d * 60
t =  pk + pd
print('Você usou o por {} dias e rodou {} km'.format(d, k))
print('Logo o valor das diarias foi de {} e dos km foi {} o total deu R${:.2f}'.format(pd, pk, t))