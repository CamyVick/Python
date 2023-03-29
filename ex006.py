'''
Crie um algoritmo que leia um número e mostre
o seu dobro, triplo e raiz quadrada
'''
n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(' O dobro de {} equivale a {}.'.format(n, d))
print(' O triplo de {} equivale a {}.'.format(n, t))
print(' E a raiz de {} equivale a {:.2f}.'.format(n, r))
#---> Outra forma seria
# print(' O triplo de {} equivale a {}\n A raiz de de {} equivale a {}'.format(n, n*3, n, n**(1/2)))
# print(' O triplo de {} equivale a {}\n A raiz de de {} equivale a {}'.format(n, n*3, n, pow(1/2)))
# {:.2f}--> 2 casas decimais flutuantes