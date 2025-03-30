# DESAFIO 05

""" Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for impar desconsidere-o. """

soma = 0

for i in range(1, 7):
    numero = int(input(f"🔍 Digite o {i}º número inteiro: ")) # para não digitar num1, num2, num3...
    if numero % 2 == 0:
       soma += numero

print(f"\nA soma dos números inteiros \033[1;34mpares\033[0m é \033[1;32m{soma}\033[0m.")