# Faça um programa que leia um número e mostre na tela o seu sucessor e o seu antecessor.

valor = int(input("Digite um valor: "))
sucessor = valor + 1
antecessor = valor - 1
print("O sucessor de {} é {} e o antecessor é {}".format(valor, sucessor, antecessor))