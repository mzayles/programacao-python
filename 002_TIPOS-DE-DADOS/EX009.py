# DESAFIO 009

""" Crie um programa e declare uma constante PI utilizando 4 casas
decimais. Dados o raio e a altura, calcule e apresente o volume de um
objeto cilíndrico.
Fórmula: volume = PI * r² * altura """

PI = 3.1415
raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

print(f"\nO volume do objeto cillíndrico é de \033[1;34m{PI * (raio ** 2) * altura:,.2f}cm³\033[0m.")