'''
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,  
só que agora utilizando um laço for.
'''
n = int(input('Digite um numero e veja a tabuada dele: '))
for c in range(1,10+1):
    n1=n*c
    print('{} x {:2} = {}'.format(n,c,n1))
