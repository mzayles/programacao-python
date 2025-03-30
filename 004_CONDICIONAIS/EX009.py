# DESAFIO 009

""" Escreva um programa para aprovar um empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai
pagar.

Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será
negado. """

valor_casa = float(input("Informe o \033[4mvalor\033[0m da casa: "))
salario = float(input("Informe o \033[4msalário\033[0m do comprador: "))
meses = int(input("Em quantos \033[4manos\033[0m a casa será quitada: ")) * 12

valor_prestacao = valor_casa/meses
valor_excedido = salario*0.3 # salario*30/100

if valor_prestacao > valor_excedido:
    print(f"\n\033[31mNegado!\033[0m Parcela máxima: R$ {valor_excedido:,.2f}.")
    print(f"Parcela simulada: R$ {valor_prestacao:,.2f}.")
else:
    print(f"\n\033[32mAprovado!\033[0m Valor da parcela: R$ {valor_prestacao:,.2f} 💸.")