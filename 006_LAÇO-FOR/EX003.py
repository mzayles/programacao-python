# DESAFIO 003

""" Mostre a tabuada de um número que o usuário escolher. """

numero = int(input("🔎 Informe a \033[1;34mtabuada\033[0m que você deseja saber: "))
print()

for i in range(0, 11):
    print(f"   {numero} x {i} = \033[1;34m{numero * i}\033[0m")

# VERSÃO 003.1

soma = 0

for num in range(0, 501, 3):
    if num % 2 != 0:
        soma += num

print(f"{soma:,.0f}".replace(',', '.'))

# VERSÃO 003.2

tab = int(input("Digite um número: "))
for i in range(0, tab * 10 + 1, tab):
    print(i)