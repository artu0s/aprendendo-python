# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

people = 0
bigger = 0
for x in range(0, 7):
    people = 2019 - int(input("Ano de nascimento: "))
    if people >= 18:
        bigger += 1
print("Maior de idade: ", bigger)
print("Menor de idade: ", (7-bigger))