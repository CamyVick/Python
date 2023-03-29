n1 = int(input('digite um numero: '))
n2 = int(input('Digite um numero: '))
e = 0
while e != 5:
    e = int(input('''Escolha as opções:
    [1] SOMA
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA\n'''))
    if e == 1:
        soma = n1 + n2
        print('A soma foi: {}'.format(soma))
    elif e == 2:
        multi = n1*n2
        print('A multiplicação foi: {}'.format(multi))
    elif e == 3:
        if n1 > n2:
            print('{} é o maior numero: '.format(n1))
        elif n2 > n1:
            print('{} é o maior numero'.format(n2))
        else:
            print('Não hha maior pois são o mesmo número ')
    elif e == 4:
        n1 = int(input('O novo número: '))
        n2 = int(input('O novo número: '))
    elif e == 5 :
        print('Fim')
    else:
        print('Operação inexistente')
print('Fim da execução')
