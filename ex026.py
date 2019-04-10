# Faça um programa que leia um frase pelo teclado e mostre:
    # Quantas vezes aparecem a letra 'a';
    # Em que posição ela aparece pela primeira vez;
    # Em que posição ela aparece pela última vez.

frase = str(input('Digite uma frase: '))
letraA = print('Aparecem na frase {} letras a'.format(frase.count('a')))
posicaoA = print('Ela aparece pela primeira vez na posição {}'.format(frase.find('a')))
posicaoB = print('Ela aparece pela última vez na posição {}'.format(frase.rfind('a')))