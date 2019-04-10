# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

i_impar = 0
contador = 0
for num_impar in range(1, 501, 2):
    if num_impar % 3 == 0:
        i_impar += num_impar
        contador += 1
print(i_impar, contador)
