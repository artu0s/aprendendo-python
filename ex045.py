# Faça um programa que jogue jokempo com você.

import random

lista = ["Pedra", "Papel", "Tesoura"]
computador = random.randint(0,2)
minha_jogada = str(input("Escolha entre Pedra, Papel e Tesoura: [0] Pedra [1] Papel [2] Tesoura"))
print("Computador: {}".format(lista[computador]))
print("Jogador: {}".format(minha_jogada))
if computador == 0: # Pedra
    if minha_jogada == 0:
        print("Empate!")
    elif minha_jogada == 1:
        print("Você ganhou!")
    elif minha_jogada == 2:
        print("Você perdeu!")
elif computador == 1: # Papel
    if minha_jogada == 0:
        print("Você perdeu!")
    elif minha_jogada == 1:
        print("Empate!")
    elif minha_jogada == 2:
        print("Você ganhou!")
elif computador == 0: # Tesoura
    if minha_jogada == 0:
        print("Você ganhou!")
    elif minha_jogada == 1:
        print("Você perdeu!")
    elif minha_jogada == 2:
        print("Empate!")