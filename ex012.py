# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

n1 = int(input("Preço do produto: "))
n2 = int(input("Desconto: "))
desconto =  (n2/100) * n1
valorTotal = n1-desconto
print("O preço do produto original é {} e com {}% de desconto fica {}.".format(n1, n2, valorTotal))