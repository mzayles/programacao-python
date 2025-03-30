# DESAFIO 004

""" Crie um programa para entrar com a base e a altura de um retângulo e imprimir
respectivamente o perímetro e a área correspondente. """

base = float(input("Digite a base do retângulo: ")) # input não aceita estilizações
altura = float(input("Digite a altura do retângulo: "))

print(f"\nO \033[4mperímetro\033[0m do retângulo é \033[1;34m{2 * (base + altura)}cm\033[0m"
      f" e sua área é \033[1;34m{base * altura}m²\033[0m.")