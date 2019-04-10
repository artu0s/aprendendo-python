# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Digite uma temperatuda em Celsius: "))
fahr = (celsius * 9/5) + 32
print("A temperatura {}C para Fahrenheit é {}".format(celsius, fahr))