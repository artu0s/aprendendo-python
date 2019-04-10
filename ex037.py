# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# 1 para binária
# 2 para octal
# 3 para hexadecimal

valor = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases: 
[1] - Binária
[2] - Octal
[3] - Hexadecimal
''')
opcao = int(input('Digite uma das opções acima: '))
if opcao == 1:
    print('O número {} convertido para binário é {}.'.format(valor, bin(valor)[2:]))
elif opcao == 2:
    print('O número {} convertido para octal é {}'.format(valor, oct(valor)[2:]))
elif opcao == 3:
    print('O número {} convertido para hexadecimal é {}'.format(valor, hex(valor)[2:]))
else:
    print('Valor inválido.')