# DESAFIO 001

""" Crie um programa que leia o nome de um bairro e diga se
ele começa ou não com o nome Santo. """

bairro = input("Digite o nome do bairro: ").lower().split()

if bairro[0] == 'santo':
    print("O nome do bairro começa com Santo 👍. ")
else:
    print("O nome do bairro não começa com Santo 👎.")

# VERSÃO 001.1

bairro = input("Digite o nome do bairro: ").lower()

if 'santo' in bairro.split()[0]:
    print("O bairro \033[1;32mcomeça\033[0m com Santo.")
else:
    print("O bairro \033[1;31mnão\033[0m começa com Santo.")

# VERSÃO 001.2

nome_bairro = input("Digite o nome do bairro: ")

if nome_bairro[:5].lower() == "santo": # por número de caracteres
    print("O bairro começa com 'Santo'.😀")
else:
    print("O bairro não começa com 'Santo'.😥")