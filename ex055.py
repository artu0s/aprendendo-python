# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

higher = 0
lower = 0
for p in range(1, 6):
    height = int(input("Peso da {} pessoa: ".format(p)))
    if p == 1:
        higher = height
        lower = height
    else:
        if height > higher:
            higher = height
        if height < lower:
            lower = height
print("Maior peso: ", higher, " Menor peso", lower)