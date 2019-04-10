# Faça um algorítimo que leia o salário e mostre seu novo salário, com 15% de aumento

salário = int(input("Digite o seu salário: "))
adicionar = (15/100) * salário
salárioTotal = salário+adicionar
print("Seu salário é {} e você recebeu um aumento de 15%, assim receberá agora {:.0f}".format(salário, salárioTotal))