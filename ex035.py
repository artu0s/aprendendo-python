# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = int(input('Tamanho da primeira reta: '))
r2 = int(input('Tamanho da segunda reta: '))
r3 = int(input('Tamanho da terceira retaL '))
# ----------

if r3 < r1+r2 or r1 < r2+r3 or r2 < r1+r3:
    print('Não é um triângulo.')
else:
    print('É um triângulo.')