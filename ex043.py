'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
IMC  mostre seu status,de acordo com a tabela abaixo

- Abaixo de 18.5: abaixo do peso
- Entre 18.5 e 25 peso idéal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- Acima de 40: Obesidade mórbida

'''
peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura: '))
formula = peso / altura**2
if formula < 18.5:
    print('{:.1f} Abaixo do peso'.format(formula))
elif formula == 18.5 or formula < 25:
    print('{:.1f} Peso idéal'.format(formula))
elif formula == 25 or formula < 30:
    print('{:.1f} Sobrepeso'.format(formula))
elif formula == 30 or formula <= 40:
    print('{:.1f} Obesidade'.format(formula))
else:
    print('{:.1f} Obesidade Mórbida'.format(formula))
