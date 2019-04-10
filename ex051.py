# Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progreção.

a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
n = a1 + (10-1) * r
for termos in range(a1, n, r):
    print("{}".format(termos), end=" -> ")
print("Fechou!")

# an = a1+(n-1)*r