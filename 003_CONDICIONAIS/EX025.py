# DESAFIO 025

""" Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade:

Se ele ainda vai se alistar ao serviço militar
Se é a hora de se alistar
Se já passou o tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou
que passou do prazo. """

ano_nasc = int(input("Digite seu ano nascimento: "))
idade = 2025 - ano_nasc

if idade < 18:
    print("\033[32mVocê ainda vai se alistar ao serviço militar!\033[0m 😇")
elif idade == 18:
    print("\033[36mÉ hora de se alistar!\033[0m 😨")
else:
    print("\033[31mJá passou o tempo do alistamento!\033[0m 🤗")