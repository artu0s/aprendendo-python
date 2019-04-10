# Faça um programa que leia a largura e a altura de uma parede em metros calcule a sua área e a quantidade de tinta
# necessaria para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2

l = float(input("Largura da parede em metros: "))
h = float(input("Altura da parede em metros: "))
area = l*h
tinta = area / 2
print("As dimensões da parede são de {}x{} = {}m²".format(l, h, area), end=". ")
print("Então a quantidade de tinta para pintar essa parede é de {} litros de tinta.".format(tinta))