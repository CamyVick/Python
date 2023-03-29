'''
Crie um progama que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possiveis sobre ela
'''
a = input('Digite Algo: ')
print('O numero primitivo desse valor é', type(a))
print('É numerico?',a.isnumeric())
print('Só tem espaços?', a.isspace())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?',a.isalnum())
print('Está em maiúsculo?',a.isupper())
print('Está em minusculo?', a.islower())
print('Está capitalizada?', a.istitle())