g = str(input('Digite o seu gênero: \nM/F:')).strip().upper()
while g != 'M' and g != 'F':
    print('A sigla digitada não é corresponte: ')
    g = str(input('\nM/F')).upper() 
if g == 'M':
    print('O gênero selecionado foi o masculino: ')
else: 
    print('O gênero selecionado foi o feminino: ')
