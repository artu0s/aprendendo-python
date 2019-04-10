# Calcule o IMC e mostre o seu status:
# Abaixo de 18.5: Abaixo do peso;
#   Entre 18.5 e 25: Peso ideal;
#       25 até 30: Sobrepeso;
#           30 até 40: Obesidade;
#               Acima de 40: Obesidade mórbida.

altura = float(input('Quanto você tem de altura: '))
peso = float(input('Qual o seu peso: '))
imc = peso/(altura**2)

print('Seu IMC é de {:.1f} e você esta'.format(imc), end=' ')
if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal.')
elif imc >= 25 and imc < 30:
    print('Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Obesidade.')
elif imc >= 40:
    print('Obesidade mórbida.')