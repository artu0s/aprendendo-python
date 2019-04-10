# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

var = '-=-'*10

print(var)
print('   Tente adivinhar o número')
print(var)

number = random.randint(0, 5)
resposta = int(input('Digite um número entre 0 e 5: '))
if resposta == number:
    print('Voce digitou o número {} e a resposta certa era {}, parabéns você acertou!.'.format(resposta, number))
else:
    print('Você errou, a sua resposta foi {} e a resposta certa era {}.'.format(resposta, number))