# DESAFIO 004

""" Crie um programa que tenha uma tupla única com 4 produtos e seus respectivos preços em sequência.
Mostre uma listagem com os nomes e preços, organizando os dados em forma tabular. """

produtos = ('Camiseta', 50, 'Calça', 79, 'Bermuda', 40, 'Blusa', 100)

for i, produto in enumerate(produtos):
    if i % 2 == 0:
        print(f"⏩ {produto.ljust(30, '.')} ", end="")
    else:
        print(f"R$ {produto:,.2f} 💸")

# VERSÃO 004.1

produtos = ('Camiseta', 50, 'Calça', 79, 'Bermuda', 40, 'Blusa', 100)

for i, produto in enumerate(produtos):
    if i%2 == 0:
        print(produto.ljust(20, '.'), end='')
    else:
        print(f"{produto:,.2f}".rjust(10, '.'))