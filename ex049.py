# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher.

tabuada = int(input("Tabuada de 1 á 10: "))
for c in range(1, 11):
    print("{} x {} = {}".format(tabuada, c, tabuada*c))