# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

from sys import exit
num = int(input("Digite um número: "))
for primo in range(2, num):
    if num % primo == 0:
        exit("O número {} é um número primo.".format(num))
print("O número {} não é um número primo.".format(num))