# Desenvolva um programa que leia seis número inteiros e mostre a soma apenas daqueles que forem pares.

soma = 0
for c in range(0, 6):
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        soma += num
print(soma)
