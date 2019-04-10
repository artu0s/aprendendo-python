# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

var = str(input("Digite seu nome: "))
print("O tipo primitivo desse valor é: ", (type(var)))
print("Seu nome está em letra maiúscula? ", var.isupper())
print("A sua resposta é formada apenas por letras?", var.isalpha())
print("A sua resposta é formada apenas por números?", var.isnumeric())
print("Seu nome está em letra minúscula? ", var.islower())
