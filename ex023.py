# Faça um programa que leia um número de 0 á 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Número de 0 á 9999: '))
print('O número escolhido foi: {}'.format(num))
n = str(num)
unidade = print('Unidade: {}'.format(n[3))
dezena = print('Dezena: {}'.format(n[2]))
centena = print('Centena: {}'.format(n[1]))
milhar = print('Milhar: {}'.format(n[0]))




