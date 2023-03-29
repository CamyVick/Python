
'''
A conferencia Nacional de Natação precisa de um programa que leia o ano de nascimento 
de um atetla e mostre sua categoria de acordo com a idade

- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
'''
from datetime import date
data = date.today().year
idade = int(input('Digite o ano que você nasceu: '))
ano = data - idade
if ano <= 9:
    print('A sua categoria é a Mirin. ')
elif ano <= 14:
    print('A sua categoria é a Infantil. ')
elif ano <= 19:
    print('A sua categoria é a Junior. ')
elif ano <= 20:
    print('A sua categoria é a Sênior. ')
else:
    print('A sua categoria é master.')