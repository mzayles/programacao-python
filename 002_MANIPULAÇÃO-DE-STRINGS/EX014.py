# DESAFIO 014

""" Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o ultimo nome separadamente.

Exemplo: Leandro Gomes Andrade

Primeiro: Leandro
Ultimo: Andrade """

nome_completo = input("Digite seu nome completo: ").split()

print(f"\033[1;32m\nPrimeiro\033[0m: {nome_completo[0].title()}")
print(f"\033[1;32mSegundo\033[0m: {nome_completo[1].title()}")

# CORREÇÃO 014.1
nome_completo = input("Digite seu nome completo: ")

print(f"\nPrimeiro nome: {nome_completo.title().split()[0]}")
print(f"Último nome: {nome_completo.title().split()[-1]}")

# CORREÇÃO 014.2 > EXEMPLO ÚLTIMO NOME
nome_completo = input("Digite seu nome completo: ")
print(f"Último nome: {nome_completo[nome_completo.rfind(' ')+1:]}")