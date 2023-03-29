'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
no final, de acordo com a média atingida:

-Média abaixo de 5.0:
reprovado
-Média entre 5.0 e 6.9:
Recuperação
-Média acima de 7.0
aprovado
'''
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota:' ))
media = (nota1+nota2)/2
if media < 5:
    print('*********************Reprovado*********************')
elif media == 5 or media < 6.9:
    print('*********************Recuperação*********************')
else:
    print('*********************Aprovado*********************')
print('Pois sua nota foi {}'.format(media))



