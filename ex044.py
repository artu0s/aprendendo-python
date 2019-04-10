# Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamente:

# Á vista dinheiro/cheque: 10% de desconto.
# Á vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

produto_valor = int(input("Digite o valor do produto: "))
# Dinheiro ou cheque
desconto = produto_valor*0.10
dinheiro_cheque = produto_valor-desconto
# A vista no cartão
desconto2 = produto_valor-0.05
avista_cartao = produto_valor-desconto2
# Até 2x no cartão
duas_cartao = produto_valor
# 3x ou mais no cartão
juros = produto_valor*0.2
tres_cartao = produto_valor+juros
print(produto_valor)
# ------------------
pagar = str(input("Qual a forma de pagamento: [A] Dinheiro/Cheque [B] Cartao: "))
if pagar == 'B' or pagar == 'b':
    selecione = str(input("Seleciona uma das opções: [A] A vista no cartão [B] 2x no cartão [C] 3x ou mais no cartão: "))
    if selecione == 'A' or selecione == 'a':
        print("Você esta pagando a vista no cartão e recebeu 5% de desconto, o valor do seu produto agora é R${:.2f}".format(avista_cartao))
    elif selecione == 'B' or selecione == 'b':
        print("Você esta pagando em 2x no cartão, o valor do seu produto é R${:.2f}".format(produto_valor))
    elif selecione == 'C' or selecione == 'c':
        print("Você esta pagando em 3x ou mais no cartão e recebeu 20% de juros, o valor do seu produto agora é R${:.2f}".format(tres_cartao))
elif pagar == 'A' or pagar == 'a':
    print("Você esta pagando no dinheiro/cheque e recebeu 10% de desconto, o valor do seu produto agora é R${:.2f}".format(dinheiro_cheque))