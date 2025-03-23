# DESAFIO 002

""" Escreva um programa que leia dois caracteres e imprima-os na tela da seguinte forma:
O usuário digitou {caractere1} e {caractere2}!. """

caractere1 = input("Digite o 1º caractere: ")
caractere2 = input("Digite o 2º caractere: ")

print(f"\nO usuário digitou {caractere1} e {caractere2}.")

# VERSÃO 002.1
caractere1 = input("Digite o primeiro caractere: ")
caractere2 = input("Digite o segundo caractere: ")

print(f"\nO usuário digitou \033[1;32m{caractere1}\033[0m " # técnica quebra de linha
      f"e \033[1;36m{caractere2}\033[0m!")