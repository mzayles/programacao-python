# DESAFIO 028

""" Escreva um programa que leia dois números inteiros e
compare- os, mostrando na tela uma mensagem:

O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais """

num1 = int(input("🔎 Digite o \033[1;34mprimeiro\033[0m valor inteiro: "))
num2 = int(input("🔎 Digite o \033[1;34msegundo\033[0m valor inteiro: "))

if num1 > num2:
    print(f"\nO primeiro número \033[1;34m({num1})\033[0m é maior.")
elif num2 > num1:
    print(f"\nO segundo número \033[1;34m({num2})\033[0m é maior.")
else:
    print(f"\nNão existe valor maior, os dois são \033[1;34miguais\033[0m.")