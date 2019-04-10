# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# Valor da casa
valor_casa = float(input('Valor da casa: '))
# Salário do comprador
salario = float(input('Salário do comprador: '))
valor_total = (30/100)*salario
# Anos para pagar
anos_pagar = int(input('Anos para pagar o imóvel: '))
meses = anos_pagar*12
# Prestação
prestacao = valor_casa/meses
if prestacao > valor_total:
    print('Empréstimo negado.')
else:
    print('Você esta comprando uma casa no valor de {}, pagará por mês {:.2f} e demorará {} meses para concluir a compra.'.format(valor_casa, prestacao, meses))