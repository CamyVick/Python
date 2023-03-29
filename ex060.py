num = int(input('Digite um numero e veja seu fatorial: '))
fact = 1
if num <= 0:
    print('0 não tem fatorial ')
else:
    while(num > 1):
        fact*=num
        num -=1
print('O fatorial é {}'.format(fact))