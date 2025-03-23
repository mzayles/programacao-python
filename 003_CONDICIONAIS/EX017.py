# DESAFIO 017

""" Crie um programa que leia o nome de uma pessoa e diga se ela
tem "Silva" no nome. """

nome = input("Digite seu nome: ").title().split()

if nome[1] == 'Silva':
    print("Você tem \033[1;32mSilva033[0m no nome 👍.")
else:
    print("Você não tem \033[1;32mSilva\033[0m no nome 👎.")

# VERSÃO 017.1
nome = input("Digite seu nome: ").title().split() # é necessário transformar em lista, o IN aceitaria "silvano"

if 'Silva' in nome:
    print("Tem Silva.")
else:
    print("Não tem Silva.")

# VERSÃO 017.2
nome = input("Digite seu nome: ").lower().split()

if 'silva' in nome:
    print("Você \033[1;32mtem\033[0m Silva no nome.")
else:
    print("Você \033[1;31mnão tem\033[0m Silva no nome.")