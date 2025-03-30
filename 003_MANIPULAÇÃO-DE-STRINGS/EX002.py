# DESAFIO 002

""" Faça um programa que leia um numero de quatro dígitos entre 1000
a 9999 e mostre na tela cada um dos dígitos separados.

Ex: Digite um numero: 1979

Unidade: 9
Dezena: 7
Centena: 9
Milhar: 1 """

numero = input("Digite um número de quatro dígitos: ")

print(f"\n[Unidade: {numero[0]}")
print(f"Dezena: {numero[1]}")
print(f"Centena: {numero[2]}")
print(f"Milhar: {numero[3]}")