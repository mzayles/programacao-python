# DESAFIO 005

""" Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
ele foi multado.

A multa custará R$ 7,00 por cada Km acima do limite. """

velocidade = float(input("Informe a \033[4mvelocidade\033[0m (Km/h) do carro: "))

if velocidade > 80:
    print(f"Você ultrapassou a velocidade de \033[34m80 Km/h\033[0m por estar a \033[36m{velocidade} Km/h\033[0m, sua multa custará \033[34mR$ {(velocidade - 80) * 7:,.2f}\033[0m.")
else:
    print("Não houve multas, siga em paz 🙂.")