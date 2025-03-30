# DESAFIO 001

""" Crie um programa que tenha uma tupla totalmente preenchida com
uma contagem por extenso, de um até vinte.

Seu programa deverá ler um número pelo teclado (entre 1 e 20) e
mostra-lo por extenso. """

numerosExtenso = (
    'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez','Onze','Doze',
    'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

numero = int(input("🔎 Digite um \033[4mnúmero\033[0m entre 1 e 20: "))

for indice, numeroExtenso in enumerate(numerosExtenso):
    indice += 1

    if indice == numero:
        print(f"O número \033[1;32m{numero}\033[0m por extenso é \033[1;32m{numeroExtenso.lower()}\033[0m.")

# VERSÃO 001.1

numero = int(input("Digite um número entre 1 e 20: "))
print(f"\nNúmero por extenso: {numerosExtenso[numero - 1].lower()}.")

# VERSÃO 001.2

print(f"\nNúmero por extenso: {numerosExtenso[int(input('Digite um número entre 1 e 20: '))-1]}")