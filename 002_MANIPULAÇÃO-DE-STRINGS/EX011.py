# DESAFIO 011

""" Crie um programa que leia o nome completo de uma pessoa e mostre:
 	O nome com todas as letras maiúsculas
 	O nome com todas as letras minúsculas
 	Quantas letras ao todo (sem considerar espaços)
 	Quantas letras tem o primeiro nome """

nome_completo = input("Digite seu \033[4mnome completo\033[0m: ")

print()
print(nome_completo.upper())
print(nome_completo.lower())
print(len(nome_completo.replace(' ', ''))) # excluir os espaços da frase
print(len(nome_completo.split()[0])) # split: criar uma lista e seus respectivos índices

# VERSÃO 011.1
nome_completo = input("Digite seu nome completo: ")

print(nome_completo.upper())
print(nome_completo.lower())

nome = nome_completo.split()
print(len(nome[0]+nome[1]))
print(len(nome_completo.split()[0]))

# VERSÃO 011.2

nome_completo = input("Digite seu nome completo: ")

print(nome_completo.upper())
print(nome_completo.lower())
print(len(nome_completo)-nome_completo.count(' '))
print(len(nome_completo.split()[0]))