# DESAFIO 004

""" Escreva um programa que faça o computador sortear um
número inteiro entre 1 e 3 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou
perdeu.

Biblioteca necessária:
import random
random.randint(0,1000) """

import random

computador = random.randint(1, 3)
usuario = int(input("Adivinhe o número escolhido pelo computador entre 1 e 3: "))

if usuario == computador:
    print("\033[32mParabéns, você acertou! 😁")
else:
    print("\033[31mQue pena, você errou! 😪")