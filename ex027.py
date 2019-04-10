# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.﻿

nome = str(input('Seu nome completo: '))
dividido = nome.split()
primeiro = print('O primeiro nome é {}'.format(dividido[0]))
segundo = print('O segundo nome é {}'.format(dividido[1]))