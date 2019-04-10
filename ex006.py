# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

valor = int(input("Digite um valor: "))
dobro = valor * 2
triplo = valor * 3
raiz = valor**(1/2)
print("O dobro de {} é {}, o tripo é {} e a raiz quadrada {:.0f}".format(valor, dobro, triplo, raiz))