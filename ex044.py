'''
Elabore um programa que calcule o valor a ser pago por um produto considerado 
o seu preço normal e condição de pagamento:

- Á vista Dinheiro/Cheque: 10% de desconto
- Á vista no cartão: 5% de desconto
- Em até 2x no Cartão: preço normal
- 3x ou mais no Cartão :20% de juro
'''
valor = float(input('Digite o valor do produto desejado: '))
pg = int(input(""" Escolha sua forma de pagamento:
1 - Dinheiro ou Cheque
2 - A vista no Cartão
3 - Até 2x no Cartão
4 - 3x ou mais Cartão
"""))
dinheiro = valor - (valor*0.10)
cartao1 = valor - (valor*0.05)
cartao2 = valor
cartao3 = valor + (valor*0.20)
if pg == 1:
    print('O valor final foi: {}'.format(dinheiro))
elif pg == 2:
    print('O valor final foi: {}'.format(cartao1))
elif pg == 3:
    print('O valor final foi: {}'.format(cartao2))
elif pg == 4:
    print('O valor finnal foi: {}'.format(cartao3))
else:
    print('A opção selecionada não existe')
