# DESAFIO 003

""" Faça um programa que leia uma frase pelo teclado e mostre:
    Quantas vezes aparece a letra "A"
    Em que posição ela aparece a primeira vez
    Em que posição ela aparece a ultima vez """

frase = input("\033[1;34mDigite uma frase: \033[0m").lower()

print(f"\nExistem \033[1;34m{frase.count('a')}\033[0m letras A na frase.")
print(f"O primeiro A aparece na posição \033[1;34m{frase.find('a') + 1}ª\033[0m.") # soma + 1 se não o índice impresso será 0
print(f"O último A aparece na posição \033[1;34m{frase.rfind('a') + 1}ª\033[0m.")

# VERSÃO 003.1

frase = input("Digite uma frase: ").lower()

print(f"\nA frase tem {frase.count('a')} letras A!")
print(f"Letra A 1ª vez na {frase.find('a')+1}ª posição!")
print(f"Letra A última vez na {frase.replace(' ', '').rfind('a')+1}ª posição!")