# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Velocidade do carro em Km/h: '))
print('Você estava a {}Km/h.'.format(velocidade))
multa = (velocidade-80)*7
if velocidade > 80:
    print('Você foi multado e terá que pagar R${}.'.format(multa))
else:
    print('Você não foi multado.')