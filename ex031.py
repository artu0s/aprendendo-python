# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual a distância da viagem: '))
v1 = distancia * 0.50
v2 = distancia * 0.45
if distancia <= 200:
    print('O preço da viagem será de R${}.'.format(v1))
else:
    print('O preço da viagem será de R${}.'.format(v2))