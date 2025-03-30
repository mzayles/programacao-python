# DESAFIO 001

""" Faça um programa que leia o sexo de uma pessoa, mas só aceite os
valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até
ter um valor correto. """

while True:
    sexo = input("🔎 Informe seu sexo. Digite (M) para \033[1;34mmasculino\033[0m ou (F) para \033[1;31mfeminino\033[0m: ").upper()

    if sexo != 'M' and sexo != 'F':
        print("\nDeixa de besteira, só vale M e F!")
        print("Informe novamente:\n")
        continue

    if sexo == "M":
        print("✅ Seu sexo é \033[1;34mmasculino\033[0m!")
        break
    if sexo == "F":
        print("✅ Seu sexo é \033[1;31mfeminino\033[0m!")
        break