# DESAFIO 007

""" Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos. """

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f"✅ Digite o \033[1;34m{i}º\033[0m peso: "))

    if i == 1:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f"\nO \033[1;34mmaior\033[0m peso é: {maior:,.2f}")
print(f"O \033[1;34mmenor\033[0m peso é: {menor:,.2f}")

# VERSÃO 007.1

maior = float('-inf')
menor = float('inf')

for i in range(1, 6):
    peso = float(input(f"Digite o {i}º peso: "))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f"\nMaior peso: {maior:,.1f} Kls")
print(f"Menor peso: {menor:,.1f} Kls")