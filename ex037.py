'''
Escreva um programa que leia um número intiro qualquer e peça par o usuário escolher
qual séra o base de conversão:

- 1 para Binario
- 2 para Octal
- 3 para Hexadecimal
'''
print('\nNesse programa iremos praticar a conversão numérica')
a = int(input('Escreva aqui o numero em decimal desejado: '))
b = int(input('''Aora escolha o formato que deseja: 
1 - Binário 
2 - Octal
3 - Hexadecimal
\n'''))

if b == 1:
    print('\nO número {} em binario é: {}'.format(a, bin(a)[2:]))

elif b == 2:
    print('\nO número {} em Octal é: {}'.format(a, oct(a)[2:]))
elif b == 3:
    hx = str(hex(a))
    print('\nO número {} em Hexadecimal é: {}'.format(a, hex(a)[2:]))
else:
    print('\nOpção inexistente')