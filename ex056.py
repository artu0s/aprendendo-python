idade_media = 0
velho = 0
mulheres = 0
for p in range(1, 5):
    print("Pessoa {}".format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    # Idade média //
    idade_media += idade / 4
    # Mais velho //
    if sexo == "M" or sexo == "m":
        if p == 1:
            velho = idade
        else:
            if velho < idade:
                velho = idade
    # Mulheres com menos de 20 anos //
    if sexo == "F" or sexo == "f":
        if idade < 20:
            mulheres += 1
print("""
A idade média é {},
O homem mais velho tem {} anos,
A quantidade de mulheres com menor de 20 anos é {}.
""".format(idade_media, velho, mulheres))
