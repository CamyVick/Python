'''
Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.
'''
med = float(input('Escreva uma distância em metros: '))
km = med /1000
hm =med / 100
dam = med / 10
dm = med * 10
cm = med * 100
mm = med * 1000

print('A medida de {:.2f}m equivale a: '.format(med))
print(' {} km \n {} hm \n {} dam'.format(km, hm, dam))
print(' {} dm \n {} cm \n {} mm'.format(dm, cm, mm))