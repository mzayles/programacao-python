# DESAFIO 006

""" Crie um programa que leia um número inteiro e mostre na tela
se ele é PAR ou IMPAR. """

numero_inteiro = int(input("Digite um número inteiro: "))

if numero_inteiro % 2 == 0:
    print("O número é \033[32mpar\033[0m!")
else:
    print("O número é \033[32mímpar\033[0m!")