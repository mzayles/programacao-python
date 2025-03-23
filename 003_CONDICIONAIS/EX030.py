# DESAFIO 030

""" Escreva um programa que leia um número inteiro e peça para o
usuário escolher qual será a base de conversão:

    1 para binário bin()
    2 para octal oct()
    3 para hexadecimal hex() """

numero_inteiro = int(input("Digite um número inteiro e escolha a base de conversão: "))
conversao = int(input("""
    [1] para \033[1;32mbinário\033[0m bin()
    [2] para \033[1;32moctal\033[0m oct()
    [3] para \033[1;32mhexadecimal\033[0m hex()
\n"""))

if conversao == 1:
    print(f"Número \033[1;33m{numero_inteiro}\033[0m para binário: \033[1;32m{bin(numero_inteiro)}\033[0m.")
elif conversao == 2:
    print(f"Número \033[1;33m{numero_inteiro}\033[0m para binário: \033[1;32m{oct(numero_inteiro)}\033[0m.")
elif conversao == 3:
    print(f"Número \033[1;33m{numero_inteiro}\033[0m para binário: \033[1;32m{hex(numero_inteiro)}\033[0m.")
else:
    print("Inválido!")