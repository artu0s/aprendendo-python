# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = R$3,27

real = int(input("Quantos reais você tem: "))
dolar = real / 3.27
print("Você pode comprar US${:.0f} dólares e alguns centavos.".format(dolar))