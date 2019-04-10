# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:
# - Se ele ainda vai se alistar ao serviço militar;
#   - Se é hora de se alistar;
#     - Se já passou do tempo do alistamento.
# O programa deverá mostrar também o tempo que falta ou que passou do prazo.

ano_nascimento = int(input('Em que ano você nasceu: '))
idade_real = (-ano_nascimento)+2019
prazo1 = idade_real-18
prazo2 = 18-idade_real

if idade_real > 18:
    print('Ele não pode mais se alistar pois já tem {} anos.'.format(idade_real), '\n', 'E já se passaram {} anos para fazer o alistamento.'.format(prazo1))
elif idade_real < 18:
    print('Ele ainda pode se alistar pois tem {}.'.format(idade_real), '\n', 'E ainda falta ou faltam {} anos para fazer o alistamento'.format(prazo2))
elif idade_real == 18:
    print('Você pode se alistar.')
