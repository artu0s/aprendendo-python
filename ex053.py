"""
DESAFIO 053: Detector de Palíndromo
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""
frase = str(input("Frase: ")).replace(" ", "")
inverso = " "
for polindromo in range (len(frase) + 1, -1, -1):
    inverso += frase[polindromo]
print(inverso, polindromo)

