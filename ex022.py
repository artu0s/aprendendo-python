# Crie um programa que leia o nome completo de uma pessoa e mostre:
    # O nome com todas as letras maiúsculas
    # O nome com todas as letras minúsculas
    # Quantas as letras ao todo (sem considerar espeços)
    # Quantas letras tem o primeiro nome

nome = str(input('Qual o seu nome inteiro: '))
print('Seu nome em letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras ao todo: {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de letras no primeiro nome: {}'.format(nome.find(' ')))
