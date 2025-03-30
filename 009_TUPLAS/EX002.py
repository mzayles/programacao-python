# DESAFIO 002

""" Crie um programa que gere cinco números aleatórios para uma tupla.
Mostre a listagem de números gerados, indique o menor e o maior valor. """

import random

# alimentar uma lista e depois convertê-lá para tupla
lista = []
for x in range(5):
    lista.append(random.randint(1, 20))

# lista convertida em tupla
tupla = tuple(lista)
print(tupla)
print(f"Maior: {max(tupla)}")
print(f"Menor: {min(tupla)}")

# VERSÃO 002.1

import random

# repetir essa linha 5 vezes
tupla = tuple(random.randint(1, 20) for x in range(5))

print(tupla)
print(f"Maior: {max(tupla)}")
print(f"Menor: {min(tupla)}")