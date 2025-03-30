# DESAFIO 001

""" Faça um programa que leia 5 valores numéricos e
guarde-os em uma lista. No final, mostre qual foi
o maior e o menor valor digitado e as suas respectivas posições na lista. """

lista = []

for i in range(5):
    numero = float(input(f"🔎 Digite o {i + 1}º número: "))
    lista.append(numero)

print(f"\n✅ O \033[1;34mmaior\033[0m valor é {max(lista)} e seu \033[1;34míndice\033[0m é {lista.index(max(lista))}.")
print(f"✅ O \033[1;34mmenor\033[0m valor é {min(lista)} e seu \033[1;34míndice\033[0m é {lista.index(min(lista))}.")