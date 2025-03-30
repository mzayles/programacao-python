# DESAFIO 005

""" Escreva um programa que converta valores entre diferentes moedas.
O usuário deve inserir o valor em reais e selecionar a moeda para conversão:
D (Dólar), E (Euro), ou L (Libra). Utilize match case para aplicar a conversão
correta com base nas taxas fictícias fornecidas a seguir:

1 Real = 0.18 Dólar
1 Real = 0.16 Euro
1 Real = 0.13 Libra

Símbolos: $ € £ """

valor = float(input("🔎 Insira o valor em \033[1;32mR$\033[0m e escolha a moeda para conversao: "))

moeda = input("""
    \033[1;32m[D]\033[0m Dólar
    \033[1;32m[E]\033[0m Euro
    \033[1;32m[L]\033[0m Libra
\n""").upper()

match moeda:
    case _ if moeda == "D":
        print(f"💰 R$ {valor:,.2f} convertido para \033[1;32mdólar\033[0m é $ {valor * 0.18:,.2f}.")
    case _ if moeda == "E":
        print(f"💰 R$ {valor:,.2f} convertido para \033[1;32meuro\033[0m é € {valor * 0.16:,.2f}.")
    case _ if moeda == "L":
        print(f"💰 R$ {valor:,.2f} convertido para \033[1;32mlibra\033[0m é £ {valor * 0.13:,.2f}.")
    case _:
        print("❌ Escolha uma opção válida!")