'''
Refaça o desafio 035 dos triângulo, acrescentando o recurso de motrar que tipo 
de triagulo será formado

- Equilatero: Todo os lados iguais. 
- Isoceles: Dois lados iguais.
- Escaleno: Todos os lados diferentes.
'''
print('=*=' * 20)
r1 = float(input('O primeiro segmento: '))
print('=*=' * 20)
r2 = float(input('O segundo segmento: '))
print('=*=' * 20)
r3 = float(input('O terceiro segmento: '))
print('=*=' * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM formar um triângulo:')
    if r1 == r2 == r3:
        print('Equilatero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else: 
        print('Isóceles')
else:
    print('Os segmentos NÂO PODEM formar um triângulo')