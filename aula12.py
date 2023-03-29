nome = str(input('Qual é o seu nome? '))
if nome=='Camilly':
    print('Que lindo nome!')
elif nome=='Pedro' or nome=='Maria' or nome=='João':
    print('Seu nome é muito popular no Brasil.')
elif nome in 'Ana claudia jessica Gardenia':
    print('Seu nome é femenino. ')
else:
    print('Seu nome é bem comum.')
print('Tenha um bom dia, {} !'.format(nome))