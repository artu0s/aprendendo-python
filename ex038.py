# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro é maior;
#   - O segundo é maior;
#      - Não existe valor maior, os dois são iguais.

val = int(input('Primeiro número: '))
val2 = int(input('Segundo número: '))
if val > val2:
    print('O número {} é maior que o {}, portanto o primeiro número é o maior.'.format(val, val2))
elif val < val2:
    print('O número {} é maior que o {}, portanto o segundo número é o maior.'.format(val2, val))
else:
    print('O número {} e o número {} são iguais, portanto não existe valor maior.'.format(val, val2))