# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.

import math

ang = float(input("Digite um ângulo: "))
seno = math.sin(ang)
cosseno = math.cos(ang)
tang = math.tan(ang)
print("O ângulo {} tem o seno de {}, cosseno de {} e tangente de {}".format(ang, seno, cosseno, tang))