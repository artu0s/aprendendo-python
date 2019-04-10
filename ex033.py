# Faça um programa que leia três números e mostre qual e o maior e o menor.

# Pedindo os números
num = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))
# ------------
if num > num2 and num > num3:
    maior = num
if num2 > num and num2 > num3:
    maior = num2
if num3 > num and num3 > num2:
    maior = num3
print('O maior número é o {}.'.format(maior))
#-------------
if num < num2 and num < num3:
    menor = num
if num2 < num and num2 < num3:
    menor = num2
if num3 < num and num3 < num2:
    menor = num3
print('O menor número é o {}.'.format(menor))