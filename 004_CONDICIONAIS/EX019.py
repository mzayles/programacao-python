# DESAFIO 019

""" Faça um programa que leia um ano qualquer e mostre se ele é
BISSEXTO.
O ano bissexto ocorre a cada 4 anos (exceto em anos múltiplos
de 100 que não são múltiplos de 400) """

ano = int(input("Digite o \033[4mano\033[0m: "))

if ano % 4 == 0:
    if ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} é \033[1;32mbissexto\033[0m!")
    else:
        print(f"O ano {ano} não é \033[1;32mbissexto\033[0m!")
else:
    print(f"O ano {ano} não é \033[1;32mbissexto\033[0m!")