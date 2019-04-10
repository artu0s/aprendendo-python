# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

percorrido = int(input("A quantidade de KM percorrido: "))
alugado = int(input("A quantidade de dias com o carro alugado: "))
km = 0.15 * percorrido
dia = 60 * alugado
total = km + dia
print("O carro percorreu {}Km e o total a pagar é de R${:.2f}".format(percorrido, km), end=". ")
print("O número de dias com o carro alugado foi de {} dias e o total a pagar é de R${}".format(alugado, dia), end=". ")
print("Somando tudo você ira pagar R${:.2f} por tudo.".format(total))
