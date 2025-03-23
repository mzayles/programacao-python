# DESAFIO 015

""" Refazer o DESAFIO 03 escolhendo a letra para contar e desconsiderar espaços. """

frase = input("\033[1;34mDigite uma frase: \033[0m").lower().replace(' ', '')
letra = input("\033[1;34mDigite a letra para contar: \033[0m")

print(f"\nExistem \033[1;34m{frase.count(letra)}\033[0m letras {letra} na frase.")
print(f"O primeiro {letra} aparece na posição \033[1;34m{frase.find(letra) + 1}ª\033[0m.")
print(f"O último {letra} aparece na posição \033[1;34m{frase.rfind(letra) + 1}ª\033[0m.")