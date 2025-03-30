# DESAFIO 002

""" Faça um programa onde o computador vai “pensar” em um número entre 1 a 10.
O jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer. """

import random

computador = random.randint(1, 10)
palpites = 0

while True:
    usuario = int(input("Qual foi o \033[1;34mnúmero escolhido\033[0m pelo computador entre 1 e 10: "))

    if usuario != computador:
        palpites += 1
        print("\n💔 \033[1;31mQue pena, você errou!\033[0m \033[1mTente novamente:\033[0m ")
        continue
    if usuario == computador:
        print("\n✅ \033[1;32mParabéns, você acertou!\033[0m")
        if palpites > 0:
            print(f"🔎 Quantidade de palpites: {palpites}" if palpites > 0 else '')
        break

# VERSÃO 002.1

import random

pc = random.randint(1, 10)
palpites = 1

while True:
    n = int(input("Adivinhe o número que o computador pensou (1 a 10):  "))
    if n == pc:
        print(f"\n\033[32mParabéns, você adivinhou com {palpites} palpite(s).\n 😄")
        break
    else:
        print("\n\033[31mErrou!\n\033[0m 😒")
        palpites += 1

pc = random.randint(1, 10)
palpites = 1

while True:
    n = int(input("Adivinhe o número que o computador pensou (1 a 10):  "))
    if n == pc:
        print(f"\n\033[32mParabéns, você adivinhou com {palpites} palpite(s).\n 😄")
        break
    else:
        print("\n\033[31mErrou!\n\033[0m 😒")
        palpites += 1