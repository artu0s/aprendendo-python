# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar

numero = int(input('Digite um número: '))
par = (numero % 2)
if par == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')