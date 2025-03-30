# DESAFIO 002

""" Com a lista do DESAFIO anterior, exiba uma lista com o nome da pessoa e o que ela come. """

for comida in almoco:
    print(f"\033[1;32m{comida['nome']}\033[0m come {comida['comida'].lower()}. 🥪")