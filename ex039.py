'''
Faço um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade

-Se ele ainda vai se alistar ao serviço militar
-Se é a hora de se alistar
-Se já passouu do tempo de alistamento

o programa também deverá mostrar o tempo que falta ou se passou do prazo
'''
from datetime import date
nome = str(input('Qual o seu nome: ').title())
idade = int(input('Em que ano você nasceu: '))
ano = date.today().year
genero = int(input(''' Qual o seu gênero:
1 - Feminino
2 - Masculino
'''))
calculo = ano - idade
if genero == 1:
    print('Seu alistamento não é necessário')

elif calculo <=17:
    anos1= 18 - calculo
    print("Sr. {} ainda falta {} anos para a data de se alistar".format(nome,anos1))
elif calculo==18:
    print('Sr. {} está no momento do seu alistamento'.format(nome))
else:
    anos2= calculo - 18
    print('Sr. {} seu alistamento deveria ter sido feito a {} atrás.'.format(nome,anos2))
