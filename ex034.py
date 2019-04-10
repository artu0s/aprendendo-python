# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salário superiores a R$1250, aumento de 10%
# Para inferiores, aumento de 15%

salario = float(input('Digite o seu salário: '))
a1 = (10/100) * salario
total1 = a1 + salario
a2 = (15/100) * salario
total2 = a2 + salario
if salario > 1250:
    print('O seu salário foi aumentado em 10% e agora você receberá R${}.'.format(total1))
else:
    print('O seu salário foi aumentado em 15% e agora você receberá R${}.'.format(total2))