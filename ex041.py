# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:
# - Até 9 anos: Mirim
#   - Até 14 anos: Infantil
#       - Até 19 anos: Junior
#               - Até 20 anos: Sênior
#                   - Acima de 20 anos: Master

ano_nascimento = int(input('Ano de nascimento: '))
idade_concorrente = 2019-ano_nascimento
if idade_concorrente <= 9:
    print('Mirim.')
elif idade_concorrente >= 10 and idade_concorrente <= 14:
    print('Infantil')
elif idade_concorrente >= 15 and idade_concorrente <= 19:
    print('Junior')
elif idade_concorrente == 20:
    print('Sênior')
elif idade_concorrente > 20:
    print('Master')