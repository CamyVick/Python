'''
Desenvolva um progama que leia as duas notas de um aluno
e mostre sua média
'''
n1 = float(input('Nota da primeira avaliação '))
n2 = float(input('Nota da segunda avaliação '))
s = (n1 + n2) / 2
#m = s / 2

print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, s))