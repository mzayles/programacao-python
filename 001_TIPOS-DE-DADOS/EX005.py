# DESAFIO 005

""" Crie um programa que dados o valor, da taxa e o tempo, efetuar o cálculo do valor de
uma prestação em atraso.
FÓRMULA: valor da prestação + (valor da prestação * (taxa / 100) * tempo) """

valor = float(input("🔍 Digite o valor da prestação: R$ "))
taxa = float(input("🔍 Digite a taxa da prestação: "))
tempo = int(input("🔍 Digite o tempo da prestação (em meses): "))

print(f"\n✅ O valor da prestação em atraso é de \033[1mR$ {valor + (valor * (taxa / 100) * tempo):,.2f}\033[0m.")

# VERSÃO 005.1
valor = float(input("Digite o valor da prestação: R$ "))
taxa = float(input("Digite a taxa da prestação: "))
tempo = int(input("Digite a qtd de meses em atraso: "))
prestacao = valor + valor * (taxa / 100) * tempo

print(f"\nValor atualizado: R$ {prestacao:,.2f}") # formatando para casas decimais (:,.Xf)