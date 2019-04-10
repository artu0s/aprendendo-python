# Crie um programa que leia duas notas de um aluno e calcule seu média, mostrando uma mensagem no final , de acordo com a média atingida;
# - Abaixo de 5; Reprovado
# - Entre 5 e 6.9; Recuperação
# - 7 ou superior; Aprovado

mediaA = float(input('Primeira nota: '))
mediaB = float(input('Segunda nota: '))
media_total = (mediaA + mediaB)/2
cores = {
    'verde':'\33[1;32m',
    'amarelo':'\33[1;33m',
    'vermelho':'\33[1;31m'
}

if media_total < 5:
    print('{}Reprovado'.format(cores['vermelho']))
elif media_total > 5 and media_total < 6.9:
    print('{}Recuperação'.format(cores['amarelo']))
elif media_total >= 7:
    print('{}Aprovado.'.format(cores['verde']))