# Refaça o DESAFIO 035 dos triângulos, acresentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais;
# Isósceles: Dois lados iguais;
# Escaleno: Todos os lados diferentes.

r1 = int(input('Valor da primeira reta: '))
r2 = int(input('Valor da segunda reta: '))
r3 = int(input('Valor da terceira reta: '))

if r3 < r1+r2 or r1 < r2+r3 or r2 < r1+r3:
    print('É um triângulo.')
    if r1 == r2 == r3:
        print('Equilátero.')
    if r1 != r2 != r3 != r1:
        print('Escaleno.')
    else:
        print('Isósceles.')