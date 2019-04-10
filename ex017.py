# Faça um programa que leia o comprimento do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento
# hipotenusa.

import math

catetoOposto = int(input("Comprimento do Cateto Oposto: "))
catetoAdjacente = int(input("Comprimento do Cateto Adjacente: "))
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)
print("O valor do Cateto Oposto é {}, o do Cateto Adjecente é {} e juntos formam a Hipotenusa com o valor {}.".format(catetoOposto, catetoAdjacente, hipotenusa))