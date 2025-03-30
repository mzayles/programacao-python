# DESAFIO 002

""" Faça um programa que receba um número inteiro de 0 a 9.
Crie uma função que apresente o resultado da tabuada deste número. """

def tabuada(num_inteiro):
    print()
    for i in range(11):
        print(f"🔎 {num_inteiro} x {i} = {num_inteiro * i}")

tabuada(int(input("💡 Digite um número entre 0 e 9 para obter a \033[1;34mtabuada\033[0m: ")))