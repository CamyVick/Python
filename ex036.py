'''
Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa.
O programa va perguntar o valor da casa, o salario do comprador e em quantos anos
ele vai pagar
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario
então o emprestimo será negado
'''
nome = str(input('Digite o seu nome: '))
valor_casa = float(input('Qual o valor do imovel desejado: '))
salario = float(input('Qual o seu salario mensal: '))
anos = int(input('Em quantos anos pretende pagar a casa: '))

parcelas = valor_casa / (anos*12)
porcentagem = salario*0.30

if parcelas <= porcentagem :
    print('Parabens {} o seu emprestimo foi aprovado com parcelas de {:.2f} ao longo de {} anos'.format(nome,parcelas,anos))# and='' para juntar a segunda linha com a primeira#
else:
    print('''Sinto muito {} mas o seu empretimo não atingiu os requisitos necessários para a aprovação a parcela foi {} e você recebe {}'''.format(nome,parcelas,salario))
