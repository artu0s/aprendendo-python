# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

mt = int(input("Valor em metros: "))
cm = mt * 100
mm = mt * 1000
print("O valor em metros {} convertido para centímetros é {} e para milímetro {}".format(mt, cm, mm))