# DESAFIO 006

""" Crie um programa que peça ao usuário para inserir uma letra. O programa deve utilizar match case
para verificar se a letra é uma vogal. """

letra = input("Digite uma \033[1;34mletra\033[0m: ").upper()

match letra:
    case 'A' | 'E' | 'I' | 'O' | 'U':
        print(f"A letra \033[1;32m{letra}\033[0m é uma \033[34mvogal\033[0m.")
    case _:
        if letra.isalpha():
            print(f"A letra \033[1;32m{letra}\033[0m é uma \033[34mconsoante\033[0m.")
        else:
            print("\033[1;31mInválido!\033[0m")